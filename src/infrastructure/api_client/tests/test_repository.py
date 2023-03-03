from unittest import TestCase

import pytest

from infrastructure.api_client.client import APIClient
from infrastructure.api_client.repository import ApiRepository


@pytest.fixture
def api_client() -> APIClient:
    return APIClient()


@pytest.mark.vcr
def test_if_repository_get_film_by_slug(api_client: APIClient):
    repo = ApiRepository(api_client)
    result = repo.get_film("anaconda")

    assert result.name == "Anaconda"


@pytest.mark.vcr
def test_if_repository_get_latest_films(api_client: APIClient):
    repo = ApiRepository(api_client)
    result = repo.get_latest_films()

    assert len(result) == 32
