from dataclasses import dataclass
from datetime import datetime

from resource.lib.shortverse_service.domain.film.entities import Film


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
