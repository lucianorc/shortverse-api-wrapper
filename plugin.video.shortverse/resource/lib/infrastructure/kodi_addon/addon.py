import sys
from urllib.parse import urlencode, parse_qsl

import xbmcgui
import xbmcplugin

from lib.infrastructure.api_client.handlers import Handlers


_URL = sys.argv[0]
_HANDLE = int(sys.argv[1])
shortverse = Handlers()


def get_url(**kwargs):
    return "{}?{}".format(urlencode(kwargs))


def get_latest_films():
    xbmcplugin.setContent(_HANDLE, "movies")
    films = shortverse.get_latest_films()
    for film in films:
        list_item = xbmcgui.ListItem(label=film.name)
        list_item.setInfo(
            "video",
            {
                "title": film.name,
                "mediatype": "movie",
                "plot": film.description,
            },
        )
        list_item.setProperty("IsPlayable", "false")  # For now
        url = get_url(action="play", video=film.source_url)

    xbmcplugin.addSortMethod(_HANDLE, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    xbmcplugin.endOfDirectory(_HANDLE)


def router():
    get_latest_films()


def run():
    router()
