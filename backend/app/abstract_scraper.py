from typing import TypedDict, Optional
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
    @abstractmethod
    def get_options(self) -> ScraperOptions:
        pass

    async def scrape_jobs(self, db: Session)-> list[schemas.JobCreate]:
        options = self.get_options()
        jobs = []
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()

            await page.goto(options['url'])
            print(f"Scraping {options['url']}")
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
                    # existing_jobs = db.query(models.Job).filter_by(url=job_data.url).first()
                    # if not existing_jobs:
                    #     crud.add_job(db, job_data)
                    jobs.append(job_data)
                    count += 1
                    print(f"Scraped {count}/{len(offers)} offers")
                except Exception as e:
                    print(f"Error with an offer: {e}")
            await browser.close()
        return jobs