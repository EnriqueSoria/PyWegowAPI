from typing import Optional

from dataclasses import dataclass
from typing import List, Any, Union


@dataclass
class MediaEndpointParams:
    event: Union[str, int]
    purpose: int = 0
    region: str = "es-es"
    lang: str = "es"
    mongo: bool = True


@dataclass
class Thumbnails:
    s_cd: str
    m_cd: str
    s_dt: str
    m_dt: str
    l_dt: str


@dataclass
class MediaItem:
    id: int
    name: str
    image_url: Optional[str]
    description: str
    type: int
    video_url: str
    position: float
    thumbnails: Optional[Thumbnails]
    is_program_image: bool
    purpose: int


@dataclass
class MediaEndpointResponse:
    count: int
    media: List[MediaItem]
    next_page: Any
