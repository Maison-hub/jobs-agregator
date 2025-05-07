from typing import Optional
from pydantic import BaseModel, ConfigDict

class JobBase(BaseModel):
    id: Optional[int] = None
    title: str
    company: str
    url: str
    location: Optional[str] = None
    description: Optional[str] = None
    liked: Optional[bool] = False
    score: Optional[int] = None

class JobCreate(JobBase):
    pass

class Job(JobBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class UserOptions(BaseModel):
    job_title: Optional[str] = None
    profile_description: Optional[str] = None
    location: Optional[str] = None
    ollama_url: Optional[str] = None
    ollama_score_model: Optional[str] = None
    ollama_cv_model: Optional[str] = None
    franceTravail_url: Optional[str] = None
    helloWork_url: Optional[str] = None
    welcomeToTheJungle_url: Optional[str] = None