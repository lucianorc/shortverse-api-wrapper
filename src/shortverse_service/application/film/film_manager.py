from .film_storage import FilmStorage


class FilmManager(object):
    storage: FilmStorage

    def __init__(self, storage: FilmStorage) -> None:
        self.storage = storage

    def get_film(self, film_slug: str):
        return self.storage.get_film(film_slug)

    def get_latest_films(self):
        return self.storage.get_latest_films()
