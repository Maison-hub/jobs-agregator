import asyncio
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.scrapers.FranceTravailScraper import FranceTravailScraper
from app.scrapers.HelloWorkScraper import HelloWorkScraper
from app.scrapers.WelcomeToTheJungleScraper import WelcomeToTheJungleScraper

async def test_scrape_jobs():
    db: Session = SessionLocal()
    hw_scraper = HelloWorkScraper()
    ft_scraper = FranceTravailScraper()
    wttj_scraper = WelcomeToTheJungleScraper()
    try:
        jobs = []
        # jobs = await hw_scraper.scrape_jobs(db)
        # jobs.append(await ft_scraper.scrape_jobs(db))
        jobs.append(await wttj_scraper.scrape_jobs(db))
        print(f"Found {len(jobs)} jobs")
        for job in jobs:
            print(job)
    finally:
        db.close()

if __name__ == "__main__":
    asyncio.run(test_scrape_jobs())