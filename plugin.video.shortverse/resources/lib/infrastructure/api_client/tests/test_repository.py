import pytest

from resources.lib.infrastructure.api_client.client import APIClient
from resources.lib.infrastructure.api_client.repository import ApiRepository


@pytest.fixture
def repo() -> ApiRepository:
    client = APIClient()
    return ApiRepository(client)


@pytest.mark.vcr
def test_if_repository_get_film_by_slug(repo: ApiRepository):
    result = repo.get_film("anaconda")

    assert result.name == "Anaconda"


@pytest.mark.vcr
def test_if_repository_get_latest_films(repo: ApiRepository):
    result = repo.get_latest_films()

    assert len(result) == 32
