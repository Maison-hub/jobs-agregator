from sqlalchemy.orm import Session
from app import models, schemas
from typing import Optional
from . import schemas


# backend/app/crud.py
def get_jobs(db: Session, skip: int = 0, limit: int = 10, title: Optional[str] = None, score_min: Optional[int] = None, score_max: Optional[int] = None, location: Optional[str] = None, sort_by: Optional[str] = None, sort_order: Optional[str] = "asc", domain: Optional[list[str]] = None):
    query = db.query(models.Job)
    if title:
        query = query.filter(models.Job.title.ilike(f"%{title}%"))
    if score_min is not None:
        query = query.filter(models.Job.score >= score_min)
    if score_max is not None:
        query = query.filter(models.Job.score <= score_max)
    if location:
        query = query.filter(models.Job.location.ilike(f"%{location}%"))
    if domain:
        for d in domain:
            query = query.filter(models.Job.url.like(f"%{d}%"))

    total_count = query.count()

    if sort_by:
        if sort_order == "asc":
            query = query.order_by(getattr(models.Job, sort_by).asc())
        else:
            query = query.order_by(getattr(models.Job, sort_by).desc())

    offers = query.offset(skip).limit(limit).all()
    return offers, total_count

def get_job(db: Session, job_id: int):
    job = db.query(models.Job).filter(models.Job.id == job_id).first()
    return schemas.Job(
        id=job.id,
        title=job.title,
        company=job.company,
        url=job.url,
        description=job.description,
        location=job.location,
        score=job.score,
    )

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

def get_user_preferences(db: Session):
    preferences = db.query(models.UserOptions).first()
    return schemas.UserOptions(
        job_title=preferences.job_title,
        profile_description=preferences.profile_description,
        location=preferences.location,
        ollama_url=preferences.ollama_url,
        ollama_score_model=preferences.ollama_score_model,
        ollama_cv_model=preferences.ollama_cv_model,
        franceTravail_url=preferences.franceTravail_url,
        welcomeToTheJungle_url=preferences.welcomeToTheJungle_url,
        helloWork_url=preferences.helloWork_url,
    )
