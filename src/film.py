from .api import APIClient
from .dto.film import FilmDTO, FilmListDTO


class Film(object):
    def __init__(self):
        self.__client = APIClient()
        self.__session = self.__client.get_session()
        self.__path = self.__client.film_resource()

    def get(self, slug: str = None):
        if slug:
            return self.__get_by_slug(slug)

        response = self.__session.get(self.__path)
        return FilmListDTO(**response.json())

    def __get_by_slug(self, slug: str = None):
        response = self.__session.get(self.__path + f"/{slug}")
        return FilmDTO(**response.json())
