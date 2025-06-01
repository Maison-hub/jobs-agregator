from playwright.async_api import async_playwright
from sqlalchemy.orm import Session
from typing import Optional
import asyncio
from .. import schemas, models, crud
from ..abstract_scraper import AbstractScraper, ScraperOptions
from urllib.parse import quote

class HelloWorkScraper(AbstractScraper):
    def __init__(self, user_preferences: Optional[schemas.UserOptions] = None):
        super().__init__(user_preferences) 

    url = "https://www.hellowork.com/fr-fr/emploi/recherche.html?k=D%C3%A9veloppeur+web&k_autocomplete=&l=Grand+Est"
    user_preferences = None

    def __init__(self, user_preferences=None):
        self.user_preferences = user_preferences

    def forge_url(self) -> str:
        # Check if user_preferences is provided
        if self.user_preferences:
            if self.user_preferences.helloWork_url:
                return self.user_preferences.helloWork_url
            # Extract the job title and location from user preferences
            job_title = self.user_preferences.job_title if self.user_preferences and self.user_preferences.job_title else "Développeur web"
            location = self.user_preferences.location if self.user_preferences and self.user_preferences.location else "Paris"
            return f"https://www.hellowork.com/fr-fr/emploi/recherche.html?k={quote(str(job_title))}&k_autocomplete=&l={quote(str(location))}&l_autocomplete=&st=relevance&c=CDI&ray=20&d=all"
        return f"{self.url}"

    def get_options(self) -> ScraperOptions:
        return {
            "url": self.forge_url(),
            "results_selector": "ul[aria-label='liste des offres'] li",
            "title_selector": "h3 p",
            "location_selector": "div[data-cy='localisationCard']",
            "company_selector": "h3 p:nth-child(2)",
            "link_selector": "header a",
            "base_url": "https://www.hellowork.com",
            "description_selector": "div.tw-mb-8>section:first-of-type"
        }