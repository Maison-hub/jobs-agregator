from abc import ABC, abstractmethod
from sqlalchemy.orm import Session

class AbstractScraper(ABC):
    url: str

    @abstractmethod
    def scrape_jobs(self, db: Session):
        pass