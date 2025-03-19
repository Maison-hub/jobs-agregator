import asyncio
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.scrapers.FranceTravailScraper import FranceTravailScraper
from app.scrapers.HelloWorkScraper import HelloWorkScraper
from app.scrapers.WelcomeToTheJungleScraper import WelcomeToTheJungleScraper
from app import crud


async def test_scrape_jobs():
    db: Session = SessionLocal()
    # hw_scraper = HelloWorkScraper()
    ft_scraper = FranceTravailScraper()
    # wttj_scraper = WelcomeToTheJungleScraper()
    try:
        # jobs = await hw_scraper.scrape_jobs(db)
        jobs = await ft_scraper.scrape_jobs(db)
        # jobs.append(await wttj_scraper.scrape_jobs(db))
        print(f"Found {len(jobs)} jobs")
        for job in jobs:
            crud.add_job(db, job)
            print(job)
    finally:
        db.close()

if __name__ == "__main__":
    asyncio.run(test_scrape_jobs())