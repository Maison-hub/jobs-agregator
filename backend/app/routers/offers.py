import httpx
from fastapi import APIRouter, Depends, Query, HTTPException
from typing import List, Optional
from sqlalchemy.orm import Session
from app import database, models, crud ,schemas

router = APIRouter()

@router.get("/offers")
def get_offers(
        db: Session = Depends(database.get_db),
        skip: int = Query(0, ge=0),
        limit: int = Query(10, ge=1),
        title: Optional[str] = Query(None),
        score_min: Optional[int] = Query(None, ge=0, le=100),
        score_max: Optional[int] = Query(None, ge=0, le=100),
        location: Optional[str] = Query(None),
        sort_by: Optional[str] = Query(None, regex="^(title|score|location)$"),
        sort_order: Optional[str] = Query("asc", regex="^(asc|desc)$")
):
    offers, total_count = crud.get_jobs(db, skip=skip, limit=limit, title=title, score_min=score_min, score_max=score_max, location=location, sort_by=sort_by, sort_order=sort_order)
    return {"total_count": total_count, "offers": offers}

@router.get("/offers/{offer_id}")
def get_offer(offer_id: int, db: Session = Depends(database.get_db)):
    return crud.get_offer(db, offer_id)