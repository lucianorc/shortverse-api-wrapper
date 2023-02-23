from src.shortverse_wrapper import Film
from src.shortverse_wrapper.dto.film import (
    FilmDTO,
    ContentDTO,
    FilmListDTO,
    MetadataDTO,
)

import datetime
from typing import List

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
    response = Film().get("anaconda")

    assert isinstance(response, FilmDTO)
    assert isinstance(response.content, ContentDTO)
    assert isinstance(response.updated_at, datetime.datetime)
    assert isinstance(response.released_at, datetime.date)
    assert response.content.slug == "anaconda", "Film slug should be in response"
    assert set(film_keys).issubset(
        response.__annotations__
    ), "All keys should be in response"


@vcr.use_cassette("tests/vcr_cassettes/film_info.yaml")
def test_if_can_get_film_content_has_right_datetime_instances():
    response = Film().get("anaconda")
    assert isinstance(response.updated_at, datetime.datetime)
    assert isinstance(response.available_at, datetime.datetime)


@vcr.use_cassette("tests/vcr_cassettes/latest_films_list.yaml")
def test_if_can_get_latest_films_list(film_keys):
    response = Film().get()

    assert isinstance(response, FilmListDTO), "Must be an instance of FilmListDTO"
    assert isinstance(response.items, List), "Must be an instance of a List of FilmDTO"
    assert isinstance(response.items[0], FilmDTO), "Must be an instance of FilmDTO"
    assert isinstance(
        response.meta, MetadataDTO
    ), "Must be an instance of Film's MetadataDTO"
    assert set(film_keys).issubset(response.data[0].keys())
