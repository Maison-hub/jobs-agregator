import asyncio
from playwright.async_api import async_playwright
from sqlalchemy.orm import Session
from typing import Optional
from .. import schemas, models, crud
from ..abstract_scraper import AbstractScraper, ScraperOptions

class FranceTravailScraper(AbstractScraper):

    def __init__(self, user_preferences: Optional[schemas.UserOptions] = None):
        super().__init__(user_preferences) 

    url = "https://candidat.francetravail.fr/offres/recherche?lieux=44R&motsCles=D%C3%A9veloppeur+web&offresPartenaires=true&rayon=10&tri=0"

    def forge_url(self) -> str:
        if self.user_preferences.franceTravail_url:
            return self.user_preferences.franceTravail_url
        else:
            return f"{self.url}"

    def get_options(self)-> ScraperOptions :
        return {
            "url": self.forge_url(),
            "results_selector": "ul.result-list li",
            "title_selector": "h2 span",
            "company_selector": "p .subtext",
            "link_selector": "a",
            "base_url": "https://candidat.francetravail.fr",
            "description_selector": "div.description p"
        }

# Execute the scraper
# if __name__ == "__main__":
#     from sqlalchemy.orm import Session
#     from app.database import SessionLocal
#
#     scraper = WelcomeToTheJungleScraper()
#     db: Session = SessionLocal()
#
#     try:
#         asyncio.run(scraper.scrape_jobs(db))
#     finally:
#         db.close()