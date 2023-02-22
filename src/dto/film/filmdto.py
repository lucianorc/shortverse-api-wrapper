from dataclasses import dataclass
import datetime

from .content import ContentDTO


@dataclass(kw_only=True)
class FilmDTO:
    age_rating: int
    animated_url: str
    available_at: datetime.time
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
    updated_at: datetime.time
    url: str
    website: str
    content: ContentDTO
    filmmakers: None
    honor: None
    label: None
    media: None
    review_summary: None
    commendation: None
    crew: None
    link: None
    owner: None
    stat: None

    def __post_init__(self) -> None:
        self.content = ContentDTO(**self.content)
