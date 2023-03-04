import sys

import xbmcgui
import xbmcplugin

from repositories import FilmRepository


_URL = sys.argv[0]
_HANDLE = int(sys.argv[1])
film_repo = FilmRepository(_URL)


def get_latest_films():
    xbmcplugin.setContent(_HANDLE, "movies")

    films = film_repo.get_latest_films()

    xbmcplugin.addDirectoryItems(_HANDLE, films)
    xbmcplugin.addSortMethod(_HANDLE, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    xbmcplugin.endOfDirectory(_HANDLE)


def router():
    get_latest_films()


def run():
    router()
