import pytest

from resource.lib.infrastructure.api_client.handlers import Handlers


@pytest.fixture
def handlers() -> Handlers:
    return Handlers()


@pytest.mark.vcr
def test_handler_can_get_latest_films(handlers: Handlers):
    result = handlers.get_latest_films()

    assert len(result) == 32


@pytest.mark.vcr
def test_handler_can_get_film_by_slug(handlers: Handlers):
    result = handlers.get_film("anaconda")

    assert result.name == "Anaconda"
