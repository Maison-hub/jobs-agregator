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
