from abc import ABC, abstractclassmethod
from .film_dto import FilmDTO


class FilmStorage(ABC):
    @abstractclassmethod
    def get_film(self, film_dto: FilmDTO):
        pass

    @abstractclassmethod
    def get_latest_films(self):
        pass
