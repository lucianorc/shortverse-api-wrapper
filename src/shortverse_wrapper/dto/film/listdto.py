from dataclasses import dataclass
from typing import List, Dict

from .filmdto import FilmDTO


@dataclass
class MetadataDTO:
    pagination: Dict[str, str]


@dataclass(kw_only=True)
class FilmListDTO:
    data: List[Dict]
    items: List[FilmDTO] = List
    meta: MetadataDTO

    def __post_init__(self):
        self.items = [FilmDTO(**item) for item in self.data]
        self.meta = MetadataDTO(self.meta["pagination"])
