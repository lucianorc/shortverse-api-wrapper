from dataclasses import dataclass
from datetime import datetime

from shortverse_service.domain.film.entities import Film


@dataclass
class FilmDTO(object):
    id: str
    slug: str
    name: str
    description: str
    duration: int
    mature: bool
    source_url: str
    trailer_url: str

    available_at: datetime
    released_at: datetime
    updated_at: datetime

    def to_domain(self) -> Film:
        film = Film(
            self.id,
            self.slug,
            self.name,
            self.description,
            self.duration,
            self.mature,
            self.source_url,
            self.trailer_url,
            self.available_at,
            self.released_at,
            self.updated_at,
        )

        return film

    def to_dto(self, film: Film):
        film_dto = FilmDTO(
            film.id,
            film.slug,
            film.name,
            film.description,
            film.duration,
            film.mature,
            film.source_url,
            film.trailer_url,
            film.available_at,
            film.released_at,
            film.updated_at,
        )

        return film_dto
