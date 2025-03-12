from sqlalchemy import Column, Integer, String
from app.database import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(500), index=True)
    company = Column(String(200), index=True)
    location = Column(String(1000), index=True)
    url = Column(String(500), unique=True)
