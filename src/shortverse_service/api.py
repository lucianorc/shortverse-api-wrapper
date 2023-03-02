import requests


class APIClient(object):
    def __init__(self):
        self.__base_url = "https://api.shortverse.com/v1"
        self.__session = self.__create_session()

    def __create_session(self) -> requests.Session:
        session = requests.Session()
        session.params = {}
        return session

    def get_session(self):
        return self.__session

    def base_url(self) -> str:
        return self.__base_url()

    def film_resource(self) -> str:
        return "%s/film" % self.__base_url
