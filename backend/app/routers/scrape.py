import httpx
from fastapi import APIRouter, Depends, Query, HTTPException
from fastapi.responses import StreamingResponse
from typing import List, Optional
from sqlalchemy.orm import Session
from app.scrapers.WelcomeToTheJungleScraper import WelcomeToTheJungleScraper
from app.scrapers.FranceTravailScraper import FranceTravailScraper
from app.scrapers.HelloWorkScraper import HelloWorkScraper
from app import database, models, crud ,schemas

router = APIRouter()

@router.get("/test-route")
def test_route():
    return {"message": "Hello, World! testtttttt"}

async def fake_video_streamer():
    for i in range(10):
        yield f"{i}/10"

@router.get("/test-stream")
async def main():
    return StreamingResponse(fake_video_streamer())

@router.get("/scrape")
async def scrape_and_store_jobs(
    db: Session = Depends(database.get_db),
    sites: Optional[List[str]] = Query(None)
):
    if not sites or len(sites) == 0:
        raise HTTPException(status_code=400, detail="You need to specify at least one site to scrape")
    jobs = []
    if "welcometothejungle" in sites:
        scraper = WelcomeToTheJungleScraper()
        jobs += await scraper.scrape_jobs(db=db)
        await add_and_evalute_job(db, jobs)
    if "francetravail" in sites:
        scraper = FranceTravailScraper()
        jobs += await scraper.scrape_jobs(db=db)
        await add_and_evalute_job(db, jobs)
    if "hellowork" in sites:
        scraper = WelcomeToTheJungleScraper()
        jobs += await scraper.scrape_jobs(db=db)
        await add_and_evalute_job(db, jobs)
    return jobs

async def add_and_evalute_job(db: Session, jobs: [schemas.Job]):
    user_profile = "Je suis développeur frontend depuis 2 ans, spécialisé en Vue.js. Je maîtrise bien Nuxt.js, JavaScript, TypeScript, TailwindCSS et les API REST. Je recherche un poste en full remote ou avec un maximum de 1 jour sur site. Je préfère travailler dans une startup ou une entreprise innovante, avec une équipe dynamique et des projets stimulants."
    async with httpx.AsyncClient(timeout=httpx.Timeout(60.0)) as client:
        for job in jobs:
            response = await client.post(
                "http://ai:5001/evaluate-offer",
                json={
                    "job_description": job.description,
                    "user_description": user_profile
                }
            )
            print(f"Score calculé: {response.json()}")
            score = response.json()
            #check if score is a number between 0 and 100
            if isinstance(score, int) and 0 <= score <= 100:
                job.score = score
                print(f"Job: {job.title}, Score: {score}")
            print(f"Job: {job.title}, Score: INVALID SCORE: {score}")
            crud.add_job(db, job)

