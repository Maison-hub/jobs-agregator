import httpx
from typing import TypedDict, Optional, AsyncGenerator, Union
from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from playwright.async_api import async_playwright
import asyncio
from . import schemas, models, crud

class ScraperOptions(TypedDict):
    url: str
    results_selector: str
    title_selector: str
    location_selector: Optional[str]
    company_selector: str
    link_selector: str
    base_url: str
    description_selector: Optional[str]

class AbstractScraper(ABC):

    def __init__(self, user_preferences: Optional[schemas.UserOptions] = None):
        self.user_preferences = user_preferences

    @abstractmethod
    def get_options(self) -> ScraperOptions:
        pass

    async def scrape_jobs(self, db: Session, save=True, ai=False)-> AsyncGenerator:
        options = self.get_options()
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()

            await page.goto(options['url'])
            print(f"Scraping {options['base_url']}")
            yield f"Scraping {options['base_url']}\n"
            await page.wait_for_selector(options['results_selector'])

            offers_locator = page.locator(options['results_selector'])
            offers = await offers_locator.element_handles()

            print('Number of offers:', len(offers))
            count = 0
            for offer in offers:
                try:
                    title = await (await offer.query_selector(options['title_selector'])).inner_text() if await offer.query_selector(options['title_selector']) else "N/A"
                    company = await (await offer.query_selector(options['company_selector'])).inner_text() if await offer.query_selector(options['company_selector']) else "N/A"
                    link = await (await offer.query_selector(options['link_selector'])).get_attribute("href") if await offer.query_selector(options['link_selector']) else "N/A"

                    #Get Location
                    location = None
                    location_selector = options.get('location_selector')
                    if location_selector:
                        location = await (await offer.query_selector(location_selector)).inner_text() if await offer.query_selector(location_selector) else None

                    # Navigate to the offer's page to get the description
                    description = None
                    description_selector = options.get('description_selector')
                    if description_selector and link != "N/A":
                        job_page = await browser.new_page()
                        await job_page.goto(f"{options['base_url']}{link}")
                        await job_page.wait_for_selector(description_selector)
                        description = await job_page.locator(description_selector).first.inner_text()
                        await job_page.close()
                    job_data = schemas.JobCreate(
                        title=title.strip(),
                        company=company.strip(),
                        url=f"{options['base_url']}{link}",
                        description=description.strip()  if description else None,
                        location=location.strip() if location else None,
                    )
                    if ai:
                        # Call the AI model to evaluate the job
                        score = await self.get_note(job_data)
                        if score:
                            job_data.score = score
                    existing_jobs = db.query(models.Job).filter_by(url=job_data.url).first()
                    if save:
                        if not existing_jobs:
                            crud.add_job(db, job_data)
                    count += 1
                    print(f"{count}/{len(offers)}")
                    yield f"{count}/{len(offers)}\n"
                except Exception as e:
                    print(f"Error with an offer: {e}")
                    yield f"Error with an offer: {e}\n"
            await browser.close()
        yield f"Scraping completed.\n"

    @staticmethod
    async def get_note(job: schemas.Job) -> Union[int, bool]:
        user_profile = "Je suis développeur frontend depuis 2 ans, spécialisé en Vue.js. Je maîtrise bien Nuxt.js, JavaScript, TypeScript, TailwindCSS et les API REST. Je recherche un poste en full remote ou avec un maximum de 1 jour sur site. Je préfère travailler dans une startup ou une entreprise innovante, avec une équipe dynamique et des projets stimulants."
        async with httpx.AsyncClient(timeout=httpx.Timeout(60.0)) as client:
            try:
                response = await client.post(
                    "http://ai:5001/evaluate-offer",
                    json={
                        "job_description": job.description,
                        "user_description": user_profile
                    }
                )
                # Vérifiez le code de statut HTTP
                if response.status_code != 200:
                    print(f"Erreur API: {response.status_code}, contenu: {response.text}")
                    raise ValueError("Erreur API: réponse vide ou non valide.")

                # Vérifiez si la réponse est un JSON valide
                try:
                    score = response.json()
                except ValueError:
                    print(f"Réponse non valide: {response.text}")
                    raise ValueError("Erreur API: réponse au mauvais format.")

                # Vérifiez si le score est un entier entre 0 et 100
                if isinstance(score, int) and 0 <= score <= 100:
                    return score
                print(f"Score invalide: {score}")
                raise ValueError("Erreur API: score invalide.")
            except Exception as e:
                print(f"Erreur lors de la requête API: {e}")
                raise ValueError("Erreur lors de la requête API.")