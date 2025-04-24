from sqlalchemy import Column, Integer, String, Boolean, Text
from app.database import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(500), index=True)
    company = Column(String(200), index=True)
    location = Column(String(1000), index=True)
    url = Column(String(500), unique=True)
    description = Column(Text)
    liked = Column(Boolean, default=False)
    score = Column(Integer, nullable=True)

class UserOptions(Base):
    __tablename__ = "user_options"

    id = Column(Integer, primary_key=True, index=True)
    job_title = Column(String(500), index=True)
    profile_description = Column(String(1000), index=True)
    location = Column(String(1000), index=True)
    ollama_url = Column(String(500), index=True)
    ollama_score_model = Column(String(200), index=True)
    ollama_cv_model = Column(String(200), index=True)