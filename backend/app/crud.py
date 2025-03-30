from sqlalchemy.orm import Session
from app import models, schemas
from typing import Optional


# backend/app/crud.py
def get_jobs(db: Session, skip: int = 0, limit: int = 10, title: Optional[str] = None, score_min: Optional[int] = None, score_max: Optional[int] = None, location: Optional[str] = None, sort_by: Optional[str] = None, sort_order: Optional[str] = "asc"):
    query = db.query(models.Job)

    if title:
        query = query.filter(models.Job.title.ilike(f"%{title}%"))
    if score_min is not None:
        query = query.filter(models.Job.score >= score_min)
    if score_max is not None:
        query = query.filter(models.Job.score <= score_max)
    if location:
        query = query.filter(models.Job.location.ilike(f"%{location}%"))

    total_count = query.count()

    if sort_by:
        if sort_order == "asc":
            query = query.order_by(getattr(models.Job, sort_by).asc())
        else:
            query = query.order_by(getattr(models.Job, sort_by).desc())

    offers = query.offset(skip).limit(limit).all()
    return offers, total_count

def get_job(db: Session, job_id: int):
    return db.query(models.Job).filter(models.Job.id == job_id).first()

def add_job(db: Session, job: schemas.JobCreate):
    #check if job already exists
    existing_job = db.query(models.Job).filter_by(url=job.url).first()
    if existing_job:
        return existing_job
    db_job = models.Job(**job.dict())
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job
