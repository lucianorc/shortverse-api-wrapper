from datetime import datetime


class Film(object):
    id: str
    slug: str
    name: str
    director: str
    short_description: str
    long_description: str
    duration: int
    mature: bool
    source_url: str
    trailer_url: str
    fanart: str

    available_at: datetime
    released_at: datetime
    updated_at: datetime
