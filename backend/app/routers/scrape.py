from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.scrapers.WelcomeToTheJungleScraper import WelcomeToTheJungleScraper
from app.scrapers.IndeedScraper import IndeedScraper
from app import database, models, crud ,schemas

router = APIRouter()

@router.get("/test-route")
def test_route():
    return {"message": "Hello, World! testtttttt"}

@router.get("/scrape")
async def scrape_and_store_jobs(db: Session = Depends(database.get_db)):
    scraper = WelcomeToTheJungleScraper()
    #Note scrape_jobs method store in db and return jobs
    jobs = await scraper.scrape_jobs(db= db)
    return jobs

@router.get("/indeed")
async def scrape_and_store_jobs(db: Session = Depends(database.get_db)):
    scraper = IndeedScraper()
    #Note scrape_jobs method store in db and return jobs
    jobs = await scraper.scrape_jobs(db= db)
    return jobs

