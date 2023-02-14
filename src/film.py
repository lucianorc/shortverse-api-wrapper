from .api import session


class Film(object):
    def __init__(self, slug: str):
        self.slug = slug
        self._path = "https://api.shortverse.com/v1"

    def info(self):
        path = "{}/film/{}".format(self._path, self.slug)
        response = session.get(path)
        return response.json()

    @staticmethod
    def latest():
        path = "https://api.shortverse.com/v1/film"
        response = session.get(path)
        return response.json()
