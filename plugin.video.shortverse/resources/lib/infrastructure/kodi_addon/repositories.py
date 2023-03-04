from urllib.parse import urlencode
from xbmcgui import ListItem

from resources.lib.infrastructure.api_client.handlers import Handlers


class FilmRepository(object):
    def __init__(self, url: str):
        self.handlers = Handlers()
        self.url = url

    def __get_url(self, **kwargs):
        return "{}?{}".format(self.url, urlencode(kwargs))

    def get_latest_films(self) -> list:
        films = self.handlers.get_latest_films()
        response = []
        for film in films:
            list_item = ListItem(label=film.name)
            list_item.setInfo(
                "video",
                {
                    "title": film.name,
                    "originaltitle": film.name,
                    "sorttitle": film.name,
                    "director": film.director,
                    "plot": film.long_description,
                    "plotoutline": film.short_description,
                    "duration": film.duration,
                    "aired": film.released_at,
                    "path": film.source_url,
                    "trailer": film.trailer_url,
                    "mediatype": "movie",
                },
            )
            list_item.setProperty("IsPlayable", "false")  # For now
            url = self.__get_url(action="play", video=film.source_url)
            response.append((url, list_item, False))

        return response
