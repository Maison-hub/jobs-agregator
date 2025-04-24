from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app import database, models, schemas

router = APIRouter()

@router.get("/user/preferences", response_model=schemas.UserOptions)
def get_user_preferences(db: Session = Depends(database.get_db)):
    """Récupère les préférences utilisateur depuis la base de données."""
    preferences = db.query(models.UserOptions).first()
    if not preferences:
        raise HTTPException(status_code=404, detail="Aucune préférence utilisateur trouvée.")
    return preferences

@router.put("/user/preferences", response_model=schemas.UserOptions)
def update_user_preferences(preferences: schemas.UserOptions, db: Session = Depends(database.get_db)):
    """Met à jour ou crée les préférences utilisateur dans la base de données."""
    existing_preferences = db.query(models.UserOptions).first()
    if existing_preferences:
        for key, value in preferences.dict(exclude_unset=True).items():
            setattr(existing_preferences, key, value)
        db.commit()
        db.refresh(existing_preferences)
        return existing_preferences
    else:
        new_preferences = models.UserOptions(**preferences.dict())
        db.add(new_preferences)
        db.commit()
        db.refresh(new_preferences)
        return new_preferences