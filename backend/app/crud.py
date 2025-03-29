from sqlalchemy.orm import Session
from app import models, schemas

def get_jobs(db: Session):
    return db.query(models.Job).all()

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
