from playwright.async_api import async_playwright
from sqlalchemy.orm import Session
import asyncio
from .. import schemas, models, crud
from ..scraper import AbstractScraper

class IndeedScraper(AbstractScraper):
    url = "https://www.welcometothejungle.com/fr/jobs?query=developer%20web&page=1"

    async def scrape_jobs(self, db: Session):
        jobs = []
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)  # Launch the browser in headless mode
            page = await browser.new_page()

            # Navigate to the job listings page
            await page.goto(self.url)

            #print the page content
            content = await page.content()
            print(content)

            # Wait for the search results to load
            await page.wait_for_selector("div#mosaic-provider-jobcards div[data-testid='slider_item']")

            print("Page loaded")

            # Retrieve the job offers
            offers_locator = page.locator("div#mosaic-provider-jobcards div[data-testid='slider_item']")
            offers = await offers_locator.element_handles()

            print(f"Found {len(offers)} offers")
            for offer in offers:
                try:
                    title = await (await offer.query_selector("h2 a")).inner_text() if await offer.query_selector("h2 a") else "N/A"
                    company = await (await offer.query_selector("div[data-testid='text-location']")).inner_text() if await offer.query_selector("span.wui-text") else "N/A"
                    link = await (await offer.query_selector("h2 a")).get_attribute("href") if await offer.query_selector("h2 a") else "N/A"

                    #fill jobs list with dict
                    # jobs.append({"title": title, "company": company, "link": f"https://www.welcometothejungle.com{link}"})

                    job_data = schemas.JobCreate(
                        title=title.strip(),
                        company=company.strip(),
                        url=f"https://www.welcometothejungle.com{link}"
                    )
                    existing_jobs = db.query(models.Job).filter_by(url=job_data.url).first()
                    if not existing_jobs:
                        crud.add_job(db, job_data)
                        jobs.append(job_data)

                #                     print(f"{title} - {company}")
                #                     print(f"Link: https://www.welcometothejungle.com{link}")
                #                     print("-" * 50)


                except Exception as e:
                    print(f"Error with an offer: {e}")
            await browser.close()
        return jobs

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