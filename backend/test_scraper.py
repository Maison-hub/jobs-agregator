import asyncio
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.scrapers.HelloWorkScraper import HelloWorkScraper

async def test_scrape_jobs():
    db: Session = SessionLocal()
    scraper = HelloWorkScraper()
    try:
        jobs = await scraper.scrape_jobs(db)
        for job in jobs:
            print(job)
    finally:
        db.close()

if __name__ == "__main__":
    asyncio.run(test_scrape_jobs())