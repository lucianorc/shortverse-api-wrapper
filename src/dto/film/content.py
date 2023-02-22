from dataclasses import dataclass
import datetime

from src.dto import BaseDTO


@dataclass
class ContentDTO(BaseDTO):
    id: int
    type: int
    subtype: int
    title: str
    slug: str
    url: str
    content: str
    description: str
    short_title: str
    short_description: str
    color_primary: str
    color_secondary: str
    color_tertiary: str
    color_foreground: str
    allow_comments: int
    is_private: int
    publicity: int
    publicity_type: int
    is_available: bool
    available_at: datetime.time
    updated_at: datetime.time

    def __post_init__(self):
        self.available_at = self._BaseDTO__format_date_by_string(self.available_at)
        self.updated_at = self._BaseDTO__format_date_by_string(self.updated_at)
