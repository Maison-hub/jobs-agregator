from abc import ABC, abstractmethod

class AbstractScraper(ABC):
    url: str

    @abstractmethod
    def scrape_jobs(self):
        pass