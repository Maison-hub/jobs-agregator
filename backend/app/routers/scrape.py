import httpx
from fastapi import APIRouter, Depends, Query, HTTPException
from fastapi.responses import StreamingResponse
from typing import List, Optional, AsyncGenerator
from sqlalchemy.orm import Session
from app.scrapers.WelcomeToTheJungleScraper import WelcomeToTheJungleScraper
from app.scrapers.FranceTravailScraper import FranceTravailScraper
from app.scrapers.HelloWorkScraper import HelloWorkScraper
from app import database, models, crud ,schemas
from app import crud

router = APIRouter()

@router.get("/ping")
def test_route():
    return {"message": "pong"}

@router.get("/scrape")
async def scrape_and_store_jobs(
    db: Session = Depends(database.get_db),
    sites: Optional[List[str]] = Query(None),
    ai: Optional[bool] = Query(False),
) -> StreamingResponse:
    if not sites or len(sites) == 0:
        raise HTTPException(status_code=400, detail="You need to specify at least one site to scrape")
    async def scrape_generator() -> AsyncGenerator[str, None]:
        preferences = crud.get_user_preferences(db)
        if "welcometothejungle" in sites:
            yield "Starting WelcomeToTheJungle scraper...\n"
            scraper = WelcomeToTheJungleScraper(preferences)
            async for message in scraper.scrape_jobs(db=db, save=True, ai=ai):
                yield message
            yield f"Scraped jobs from WelcomeToTheJungle.\n"
        if "francetravail" in sites:
            yield "Starting FranceTravail scraper...\n"
            scraper = FranceTravailScraper()
            async for message in scraper.scrape_jobs(db=db, save=True, ai=ai):
                yield message
            yield f"Finish scraped jobs from FranceTravail.\n"
        if "hellowork" in sites:
            yield "Starting HelloWork scraper...\n"
            scraper = HelloWorkScraper()
            async for message in scraper.scrape_jobs(db=db, save=True, ai=ai):
                yield message
            yield f"Finish scraped jobs from HelloWork.\n"
        yield "Scraping completed.\n"

    return StreamingResponse(
        scrape_generator(),
        media_type="text/plain",
        headers={"X-Accel-Buffering": "no"}  # Désactive le buffering côté serveur
    )

