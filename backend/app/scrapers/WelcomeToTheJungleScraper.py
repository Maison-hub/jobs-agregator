from playwright.async_api import async_playwright
import asyncio
from ..scraper import AbstractScraper

class WelcomeToTheJungleScraper(AbstractScraper):
    url = "https://www.welcometothejungle.com/fr/jobs?query=developer%20web&page=1"

    async def scrape_jobs(self):
        jobs = []
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)  # Launch the browser in headless mode
            page = await browser.new_page()

            # Navigate to the job listings page
            await page.goto(self.url)

            # Wait for the search results to load
            await page.wait_for_selector("ul[data-testid='search-results'] li")

            print("Page loaded")

            # Retrieve the job offers
            offers_locator = page.locator("ul[data-testid='search-results'] li")
            offers = await offers_locator.element_handles()

            print(f"Found {len(offers)} offers")
            for offer in offers:
                try:
                    title = await (await offer.query_selector("h4")).inner_text() if await offer.query_selector("h4") else "N/A"
                    company = await (await offer.query_selector("span.wui-text")).inner_text() if await offer.query_selector("span.wui-text") else "N/A"
                    link = await (await offer.query_selector("a")).get_attribute("href") if await offer.query_selector("a") else "N/A"

                    #fill jobs list with dict
                    jobs.append({"title": title, "company": company, "link": link})


                    print(f"{title} - {company}")
                    print(f"Link: https://www.welcometothejungle.com{link}")
                    print("-" * 50)


                except Exception as e:
                    print(f"Error with an offer: {e}")
            await browser.close()
        return jobs

# Execute the scraper
if __name__ == "__main__":
    scraper = WelcomeToTheJungleScraper()
    asyncio.run(scraper.scrape_jobs())