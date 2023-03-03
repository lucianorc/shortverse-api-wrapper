from requests import Session

from .client import APIClient


class Film(object):
    api_session: Session
    url: str

    def __init__(self, client: APIClient):
        self.api_session = client.get_session()
        self.url = client.film_resource()

    def get_film(self, film_slug: str):
        film_url = f"{self.url}/{film_slug}"
        response = self.api_session.get(film_url)
        return response.json()

    def get_latest_films(self):
        response = self.api_session.get(self.url)
        return response.json()["data"]
