from unittest import TestCase
from typing import List

import pytest

from resources.lib.shortverse_service.application.film.film_manager import FilmManager


@pytest.mark.usefixtures("dummy_storage")
class TestFilmAggregate(TestCase):
    def test_get_film(self):
        manager = FilmManager(self.storage)
        film = manager.get_film("test-1")
        assert film.name == "Test 1"

    def test_get_latest_films(self):
        manager = FilmManager(self.storage)
        films = manager.get_latest_films()
        assert len(films) == 2
