from typing import Union

from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Venue:
    id: int
    name: str
    image_url: Optional[str]
    permalink: str
    longitude: Optional[float]
    latitude: Optional[float]
    thumbnails: Union[dict, str, None]


@dataclass
class VenueSearchResponse:
    venues: List[Venue]
    next_page: Optional[int]
    artists_count: int
    artists_max_count: bool
    companies_count: int
    companies_max_count: bool
    events_count: int
    events_max_count: bool
    venues_count: int
    venues_max_count: bool
