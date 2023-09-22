from typing import Union

from dataclasses import dataclass
from typing import List, Any, Optional


@dataclass
class Artist:
    id: int
    name: str


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
class ImageAverageColor:
    r: int
    g: int
    b: int


@dataclass
class User:
    going: bool
    tracking: bool


@dataclass
class Venue:
    id: int
    name: str
    image_url: Optional[str]
    permalink: str
    longitude: Optional[float]
    latitude: Optional[float]
    thumbnails: Union[dict, str, None]
    address: str
    directions: Optional[str]


@dataclass
class Company:
    id: int
    name: str
    permalink: str


@dataclass
class Accommodation:
    url: str
    service: str
    description: str


@dataclass
class Transport:
    url: str
    service: str
    description: str


@dataclass
class FullEvent:
    id: int
    artists: List[Artist]
    access_policy: Any
    attendance: int
    cancelation_status: int
    city: City
    closed: bool
    created: str
    description: Optional[str]
    enabled: bool
    end_date: str
    followers_count: int
    has_merchandising: bool
    image_url: Optional[str]
    links: List
    image_average_color: ImageAverageColor
    price: Optional[float]
    currency: Optional[str]
    start_date: str
    slug: str
    permalink: str
    title: str
    show_time: bool
    subtitle: str
    type: int
    user: User
    venue: Venue
    options: List
    ticket_distributions: List
    tickets_enabled: bool
    ticket_types_count: int
    tickets_count: Any
    queue_link: str
    queued: bool
    queued_web: bool
    authorization_file_url: Any
    thumbnails: Optional[dict]
    chat: int
    airbnb: bool
    index: bool
    promoter_newsletter_text: str
    promoter_newsletter_option: bool
    promoter_terms_text: Any
    promoter_terms_option: bool
    facebook_pixel_js: Any
    google_pixel_js: Any
    adwords: Any
    companies: List[Company]
    canonical: str
    purchase_url: str
    has_options: bool
    has_sales: bool
    accommodation: Accommodation
    transport: Transport
    insurance: bool
    singles: Optional[List]
    opening_hour: Optional[Any]
    access_code_needed: Optional[bool]
    access_code_valid_until: Optional[Any]
