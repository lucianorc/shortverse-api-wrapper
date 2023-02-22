from dataclasses import dataclass, fields, _MISSING_TYPE
import datetime

from .content import ContentDTO


@dataclass(kw_only=True)
class FilmDTO:
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
    crew: None
    link: None
    owner: None
    stat: None

    def __post_init__(self) -> None:
        self.content = ContentDTO(**self.content)
        self.updated_at = self.__format_date_by_string(str(self.updated_at))
        self.available_at = self.__format_date_by_string(str(self.available_at))
        self.released_at = datetime.date.fromisoformat(self.released_at)

    def __format_date_by_string(self, date: str) -> datetime.datetime | None:
        if date != "None":
            return datetime.datetime.strptime(str(date), "%Y-%m-%dT%H:%M:%S.%fZ")

        return None
