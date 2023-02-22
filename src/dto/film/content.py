from dataclasses import dataclass
import datetime


@dataclass
class ContentDTO:
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
