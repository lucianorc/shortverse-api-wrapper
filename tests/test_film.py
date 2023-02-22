from src import Film
from src.dto.film import FilmDTO, ContentDTO

from pytest import fixture
import vcr


@fixture
def film_keys():
    return {
        "age_rating",
        "id",
        "is_mature",
        "released_at",
        "source_url",
        "updated_at",
        "url",
        "content",
        "filmmakers",
        "media",
    }


@vcr.use_cassette("tests/vcr_cassettes/film_info.yaml")
def test_if_can_get_film(film_keys):
    film_instance = Film()
    response = film_instance.get("me-time-1")
    assert isinstance(response, FilmDTO)
    assert isinstance(response.content, ContentDTO)
    assert response.content.slug == "me-time-1", "Film slug should be in response"
    assert set(film_keys).issubset(
        response.__annotations__
    ), "All keys should be in response"


@vcr.use_cassette("tests/vcr_cassettes/latest_films_list.yaml")
def test_if_can_get_latest_films_list(film_keys):
    response = Film().get()

    assert isinstance(response, dict)
    assert isinstance(response["data"], list)
    assert isinstance(response["data"][0], dict)
    assert set(film_keys).issubset(response["data"][0].keys())
