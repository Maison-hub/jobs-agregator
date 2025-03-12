from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app import database, crud, models, schemas

app = FastAPI()

# Initialisation de la base de données
models.Base.metadata.create_all(bind=database.engine)

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur le scraper d'offres d'emploi"}

@app.get("/jobs", response_model=list[schemas.Job])
def get_jobs(db: Session = Depends(database.get_db)):
    return crud.get_jobs(db)
