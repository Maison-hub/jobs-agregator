from playwright.async_api import async_playwright
from sqlalchemy.orm import Session
import asyncio
from .. import schemas, models, crud
from ..abstract_scraper import AbstractScraper, ScraperOptions
from urllib.parse import urlencode, urlunparse

class WelcomeToTheJungleScraper(AbstractScraper):
    baseUrl = "https://www.welcometothejungle.com/fr/jobs?query=developer%20web&page=1"
    user_preferences = None

    def __init__(self, user_preferences=None):
        self.user_preferences = user_preferences

    def forge_url(self) -> str:
        # Check if user_preferences is provided
        if self.user_preferences:
            # Extract the job title and location from user preferences
            job_title = self.user_preferences.job_title
            location = self.user_preferences.location

            # Construct the URL with the job title and location
            self.url = f"https://www.welcometothejungle.com/fr/jobs?query={job_title}&aroundQuery={location}"
        return f"{self.url}"

    def get_options(self)-> ScraperOptions :
        return {
            "url": self.forge_url(),
            "results_selector": "ul[data-testid='search-results'] li",
            "title_selector": "h4",
            'location_selector': "i[name='location'] + p",
            "company_selector": "span.wui-text",
            "link_selector": "a",
            "base_url": "https://www.welcometothejungle.com",
            "description_selector": "div[data-testid='job-section-description']"
        }


#     async def scrape_jobs(self, db: Session):
#         jobs = []
#         async with async_playwright() as p:
#             browser = await p.chromium.launch(headless=True)  # Launch the browser in headless mode
#             page = await browser.new_page()
#
#             # Navigate to the job listings page
#             await page.goto(self.url)
#
#             # Wait for the search results to load
#             await page.wait_for_selector("ul[data-testid='search-results'] li")
#
#             print("Page loaded")
#
#             # Retrieve the job offers
#             offers_locator = page.locator("ul[data-testid='search-results'] li")
#             offers = await offers_locator.element_handles()
#
#             print(f"Found {len(offers)} offers")
#             for offer in offers:
#                 try:
#                     title = await (await offer.query_selector("h4")).inner_text() if await offer.query_selector("h4") else "N/A"
#                     company = await (await offer.query_selector("span.wui-text")).inner_text() if await offer.query_selector("span.wui-text") else "N/A"
#                     link = await (await offer.query_selector("a")).get_attribute("href") if await offer.query_selector("a") else "N/A"
#
#                     #fill jobs list with dict
#                     # jobs.append({"title": title, "company": company, "link": f"https://www.welcometothejungle.com{link}"})
#                     job_data = schemas.JobCreate(
#                         title=title.strip(),
#                         company=company.strip(),
#                         url=f"https://www.welcometothejungle.com{link}"
#                     )
#                     existing_jobs = db.query(models.Job).filter_by(url=job_data.url).first()
#                     if not existing_jobs:
#                         crud.add_job(db, job_data)
#                         jobs.append(job_data)
#
# #                     print(f"{title} - {company}")
# #                     print(f"Link: https://www.welcometothejungle.com{link}")
# #                     print("-" * 50)
#
#
#                 except Exception as e:
#                     print(f"Error with an offer: {e}")
#             await browser.close()
#         return jobs

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