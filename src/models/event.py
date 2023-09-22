from dataclasses import dataclass, field
from typing import Optional, List

from .artist import Artist
from .venue import Venue


@dataclass
class City:
    id: int
    name: Optional[str]
    administrative_division: str
    country: str
    iso_code: str
    index: bool
    timezone: str


@dataclass
class Event:
    attendance: int
    city: City
    currency: Optional[str]
    end_date: str
    id: int
    image_url: Optional[str]
    modified: Optional[str]
    permalink: str
    price: Optional[str]
    purchase_url: str
    show_time: bool
    slug: str
    start_date: str
    thumbnails: Optional[dict]
    ticket_types_count: int
    title: str
    type: int
    venue: Optional[Venue] = None
    artists: List[Artist] = field(default_factory=list)


@dataclass
class EventFeedResponse:
    count: int
    events: List[Event]
    next_page: Optional[int]


@dataclass
class EventSearchResponse:
    events: List[Event]
    next_page: Optional[int]
    artists_count: int
    artists_max_count: bool
    companies_count: int
    companies_max_count: bool
    events_count: int
    events_max_count: bool
    venues_count: int
    venues_max_count: bool
