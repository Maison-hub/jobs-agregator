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
