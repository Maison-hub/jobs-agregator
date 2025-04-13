from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app import database, models, crud ,schemas
from .routers import scrape, offers
from app.scrapers.WelcomeToTheJungleScraper import WelcomeToTheJungleScraper
import asyncio
import json
import os
from dotenv import load_dotenv

app = FastAPI()

load_dotenv()

app.include_router(scrape.router)
app.include_router(offers.router)

# Initialisation de la base de données
models.Base.metadata.create_all(bind=database.engine)

origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur le scraper d'offres d'emploi"}

@app.get("/jobs", response_model=list[schemas.Job])
def get_jobs(db: Session = Depends(database.get_db)):
    return crud.get_jobs(db)

@app.get("/test")
async def test():
    scraper = WelcomeToTheJungleScraper()
    jobs = await scraper.scrape_jobs()
    return jobs

# @app.get("/scrape")
# async def scrape_and_store_jobs(db: Session = Depends(database.get_db)):
#     scraper = WelcomeToTheJungleScraper()
#     jobs = await scraper.scrape_jobs(db= db)
#     return jobs
