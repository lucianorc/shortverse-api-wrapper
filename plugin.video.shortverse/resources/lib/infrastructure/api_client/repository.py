from resources.lib.shortverse_service.application.film.film_storage import FilmStorage
from resources.lib.shortverse_service.application.film.film_dto import FilmDTO
from .model import Film
from .client import APIClient


class ApiRepository(FilmStorage):
    film_model: Film

    def __init__(self, client: APIClient) -> None:
        self.film_model = Film(client)
        super().__init__()

    def __model_to_dto(self, film: dict):
        return FilmDTO(
            id=film["id"],
            slug=film["content"]["slug"],
            name=film["content"]["title"],
            director=film["filmmakers"]["data"][0]["name"],
            short_description=film["content"]["description"],
            long_description=film["content"]["content"],
            duration=film["duration"],
            mature=bool(film["is_mature"]),
            source_url=film["source_url"],
            trailer_url=film["trailer_url"],
            fanart=film["media"]["data"][0]["url"],
            available_at=film["available_at"],
            released_at=film["released_at"],
            updated_at=film["updated_at"],
        )

    def get_film(self, film_slug: str) -> FilmDTO:
        film = self.film_model.get_film(film_slug)
        film_dto = self.__model_to_dto(film)
        return film_dto

    def get_latest_films(self) -> list:
        films = self.film_model.get_latest_films()
        films_dto = []
        for film in films:
            films_dto.append(self.__model_to_dto(film))

        return films_dto
