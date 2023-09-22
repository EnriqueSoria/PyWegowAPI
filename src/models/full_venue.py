from dataclasses import dataclass
from typing import Any, List, Optional


@dataclass
class City:
    id: int
    name: str
    administrative_division: str
    country: str
    iso_code: str
    index: bool
    timezone: str


@dataclass
class User:
    following: bool


@dataclass
class FullVenue:
    id: int
    name: str
    image_url: Any
    permalink: str
    longitude: Optional[float]
    latitude: Optional[float]
    thumbnails: Any
    city: City
    enabled: bool
    slug: str
    user: User
    followers_count: int
    events_count: int
    index: bool
    description: Optional[str]
    address: str
    directions: Optional[str]
    facebook_pixel_js: str
    google_pixel_js: str
    adwords: str
    companies: List
    canonical: str
    links: List
