from unittest import TestCase

from shortverse_service.application.film.film_storage import FilmStorage
from infrastructure.api_client.client import APIClient
from infrastructure.api_client.repository import ApiRepository
import pytest


@pytest.fixture
def api_client() -> APIClient:
    return APIClient()


def test_if_repository_get_film_by_slug(api_client: APIClient):
    repo = ApiRepository(api_client)
    result = repo.get_film("anaconda")

    assert result.name == "Anaconda"


def test_if_repository_get_latest_films(api_client: APIClient):
    repo = ApiRepository(api_client)
    result = repo.get_latest_films()

    assert len(result) == 32
