from dataclasses import dataclass
import datetime

from .content import ContentDTO
from src.dto import BaseDTO


@dataclass(kw_only=True)
class FilmDTO(BaseDTO):
    age_rating: int
    animated_url: str
    available_at: datetime.datetime
    duration: int
    end_time: int
    has_overlay: bool
    has_password: bool
    has_preview: bool
    id: int
    is_mature: bool
    password: str
    password_match: int
    premiere_status: int
    publicity_type: int
    publicity: int
    released_at: datetime.date
    source_url: str
    trailer_url: str
    start_time: int
    updated_at: datetime.datetime
    url: str
    website: str
    content: ContentDTO
    filmmakers: None
    honor: None
    label: None
    media: None
    review_summary: None
    commendation: None
    crew: None = None
    link: None = None
    owner: None = None
    stat: None = None

    def __post_init__(self) -> None:
        self.content = ContentDTO(**self.content)
        self.updated_at = self._BaseDTO__format_date_by_string(str(self.updated_at))
        self.available_at = self._BaseDTO__format_date_by_string(str(self.available_at))
        if type(self.released_at) is str:
            self.released_at = datetime.date.fromisoformat(self.released_at)
