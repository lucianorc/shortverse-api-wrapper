from .client import APIClient
from .repository import ApiRepository


class Handlers(object):
    def __init__(self):
        self.client = APIClient()
        self.repo = ApiRepository(self.client)

    def get_film(self, film_slug: str):
        return self.repo.get_film(film_slug)

    def get_latest_films(self):
        return self.repo.get_latest_films()
