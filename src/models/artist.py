from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Artist:
    id: int
    name: str
    permalink: str


@dataclass
class ArtistSearchResponse:
    artists: List[Artist]
    next_page: Optional[int]
    artists_count: int
    artists_max_count: bool
    companies_count: int
    companies_max_count: bool
    events_count: int
    events_max_count: bool
    venues_count: int
    venues_max_count: bool
