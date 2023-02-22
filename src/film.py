from .api import APIClient


class Film(object):
    def __init__(self):
        self.__client = APIClient()
        self.__session = self.__client.get_session()

    def __url_path(self, slug: str = None):
        if slug:
            return self.__client.film_resource() + f"/{slug}"

        return self.__client.film_resource()

    def get(self, slug: str = None):
        path = self.__url_path(slug)
        response = self.__session.get(path)
        return response.json()
