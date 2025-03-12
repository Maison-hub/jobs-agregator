from typing import Optional
from pydantic import BaseModel

class JobBase(BaseModel):
    title: str
    company: str
    url: str
    location: Optional[str] = None

class JobCreate(JobBase):
    pass

class Job(JobBase):
    id: int

    class Config:
        orm_mode = True
