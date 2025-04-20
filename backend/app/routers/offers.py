import httpx
from fastapi import APIRouter, Depends, Query, HTTPException
from typing import List, Optional
from sqlalchemy.orm import Session
from app import database, models, crud ,schemas
from app.abstract_scraper import AbstractScraper

router = APIRouter()

@router.get("/offers")
def get_offers(
        db: Session = Depends(database.get_db),
        page: int = Query(1, ge=1),
        limit: int = Query(10, ge=1),
        title: Optional[str] = Query(None),
        domain: Optional[list[str]] = Query(None),
        score_min: Optional[int] = Query(None, ge=0, le=100),
        score_max: Optional[int] = Query(None, ge=0, le=100),
        location: Optional[str] = Query(None),
        sort_by: Optional[str] = Query(None, regex="^(title|score|location)$"),
        sort_order: Optional[str] = Query("asc", regex="^(asc|desc)$")
):
    skip = (page - 1) * limit
    offers, total_count = crud.get_jobs(db, skip=skip, limit=limit, title=title, score_min=score_min, score_max=score_max, location=location, sort_by=sort_by, sort_order=sort_order, domain=domain)
    total_pages = (total_count + limit - 1) // limit
    return {"total_count": total_count, "total_pages": total_pages, "current_page": page, "offers": offers}

@router.get("/offers/{offer_id}")
def get_offer(offer_id: int, db: Session = Depends(database.get_db)):
    return crud.get_job(db, offer_id)

@router.get("/offers/{offer_id}/score")
async def get_offer_score(offer_id: int, db: Session = Depends(database.get_db)):
    offer = crud.get_job(db, offer_id)
    if not offer:
        raise HTTPException(status_code=404, detail="Offer not found")
    if offer.score:
        return {"score": offer.score}
    score = await AbstractScraper.get_note(offer)
    return {"score": score}