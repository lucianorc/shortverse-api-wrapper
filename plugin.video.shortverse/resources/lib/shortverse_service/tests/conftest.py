from datetime import datetime

from pytest import fixture

from resource.lib.shortverse_service.application.film.film_storage import FilmStorage
from resource.lib.shortverse_service.application.film.film_dto import FilmDTO


@fixture(scope="class")
def dummy_films():
    films = []
    for i in range(1, 3):
        film = FilmDTO(
            id=1,
            slug=f"test-{i}",
            name=f"Test {i}",
            description=f"Test #{i}",
            duration=1,
            mature=False,
            source_url="some_url",
            trailer_url="some_url",
            available_at=datetime.now(),
            released_at=datetime.now(),
            updated_at=datetime.now(),
        )

        films.append(film)

    return films


@fixture(scope="class")
def dummy_storage(request, dummy_films: list):
    FilmStorage.__abstractmethods__ = set()

    class DummyStorage(FilmStorage):
        def get_film(self, slug: str) -> FilmDTO:
            film = list(filter(lambda f: f.slug == slug, dummy_films))
            return film[0]

        def get_latest_films(self):
            return dummy_films

    request.cls.storage = DummyStorage()
