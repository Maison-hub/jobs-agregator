from playwright.async_api import async_playwright
from sqlalchemy.orm import Session
import asyncio
from .. import schemas, models, crud
from ..abstract_scraper import AbstractScraper, ScraperOptions

class HelloWorkScraper(AbstractScraper):
    url = "https://www.hellowork.com/fr-fr/emploi/recherche.html?k=D%C3%A9veloppeur+web&k_autocomplete=&l=Grand+Est"

    def get_options(self) -> ScraperOptions:
        return {
            "url": self.url,
            "results_selector": "ul[aria-label='liste des offres'] li",
            "title_selector": "h3 p",
            "company_selector": "h3 p:nth-child(2)",
            "link_selector": "header a",
            "base_url": "https://www.hellowork.com"
        }

    # async def scrape_jobs(self, db: Session):
    #     jobs = []
    #     async with async_playwright() as p:
    #         browser = await p.chromium.launch(headless=True)
    #         context = await browser.new_context()
    #         page = await context.new_page()
    #
    #         # Navigate to the job listings page
    #         await page.goto(self.url)
    #
    #         #print the page content
    #         content = await page.content()
    #         print(content)
    #
    #         # Wait for the search results to load
    #         await page.wait_for_selector("ul[aria-label='liste des offres'] li")
    #
    #         print("Page loaded")
    #
    #         # Retrieve the job offers
    #         offers_locator = page.locator("ul[aria-label='liste des offres'] li")
    #         offers = await offers_locator.element_handles()
    #
    #         print(f"Found {len(offers)} offers")
    #         for offer in offers:
    #             try:
    #                 title = await (await offer.query_selector("h3 p")).inner_text() if await offer.query_selector("h3 p") else "N/A"
    #                 company = await (await offer.query_selector("h3 p:nth-child(2)")).inner_text() if await offer.query_selector("h3 p:nth-child(2)") else "N/A"
    #                 link = await (await offer.query_selector("header a")).get_attribute("href") if await offer.query_selector("header a") else "N/A"
    #
    #                 job_data = schemas.JobCreate(
    #                     title=title.strip(),
    #                     company=company.strip(),
    #                     url=f"https://www.hellowork.com{link}"
    #                 )
    #                 existing_jobs = db.query(models.Job).filter_by(url=job_data.url).first()
    #                 if not existing_jobs:
    #                     crud.add_job(db, job_data)
    #                     jobs.append(job_data)
    #             except Exception as e:
    #                 print(f"Error with an offer: {e}")
    #         await browser.close()
    #     return jobs

# Execute the scraper
# if __name__ == "__main__":
#     from sqlalchemy.orm import Session
#     from app.database import SessionLocal
#
#     scraper = WelcomeToTheJungleScraper()
#     db: Session = SessionLocal()
#
#     try:
#         asyncio.run(scraper.scrape_jobs(db))
#     finally:
#         db.close()