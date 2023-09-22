from dataclasses import dataclass
from typing import List, Optional


@dataclass
class User:
    following: bool


@dataclass
class Thumbnails:
    s_sq: str
    s_cd: str
    m_cd: str
    s_ver_dt: str
    ver_dt: str
    s_hor_dt: str
    m_hor_dt: str
    l_hor_dt: str


@dataclass
class ImageAverageColor:
    r: int
    g: int
    b: int


@dataclass
class Link:
    id: int
    type: int
    url: str


@dataclass
class FullArtist:
    id: int
    name: str
    enabled: bool
    events_count: int
    followers_count: int
    image_url: Optional[str]
    user: User
    slug: str
    permalink: str
    thumbnails: Optional[Thumbnails]
    created: str
    description: Optional[str]
    image_average_color: ImageAverageColor
    links: List[Link]
    modified: str
    spotify_id: Optional[str]
    index: bool
    facebook_pixel_js: str
    google_pixel_js: str
    adwords: str
    companies: List
    canonical: str
    has_merchandising: bool
