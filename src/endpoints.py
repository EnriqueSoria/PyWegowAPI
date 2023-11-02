from api_client_framework.methods import Methods
from api_client_framework.requests import RequestsEndpoint

from models.artist import ArtistSearchResponse
from models.common import SearchParams
from models.event import EventFeedResponse
from models.event import EventSearchResponse
from models.full_artist import FullArtist
from models.full_event import FullEvent
from models.full_venue import FullVenue
from models.media import MediaEndpointParams
from models.media import MediaEndpointResponse
from models.venue import VenueSearchResponse
from parsers import DataclassParser


class EventFeedEndpoint(RequestsEndpoint):
    method = Methods.GET
    url = "https://www.wegow.com/api/feed/"
    parser = DataclassParser(EventFeedResponse)

    def __init__(self, page: int | None = None):
        self.page = page or 1
        self.params = {"page": self.page}


class RetrieveEvent(RequestsEndpoint):
    method = Methods.GET
    url = "https://www.wegow.com/api/events/{event_id}/"
    parser = DataclassParser(FullEvent)

    def __init__(self, event_id: int | str):
        self.event_id = event_id

    def get_url(self) -> str:
        return self.url.format(event_id=self.event_id)


class RetrieveVenue(RequestsEndpoint):
    method = Methods.GET
    url = "https://www.wegow.com/api/venues/{venue_id}/"
    data = None
    parser = DataclassParser(FullVenue)

    def __init__(self, venue_id: int | str):
        self.venue_id = venue_id

    def get_url(self) -> str:
        return self.url.format(venue_id=self.venue_id)


class RetrieveArtist(RequestsEndpoint):
    method = Methods.GET
    url = "https://www.wegow.com/api/artists/{artist_id}/"
    data = None
    parser = DataclassParser(FullArtist)

    def __init__(self, artist_id: int | str):
        self.artist_id = artist_id

    def get_url(self) -> str:
        return self.url.format(artist_id=self.artist_id)


class SearchEvent(RequestsEndpoint):
    method = Methods.GET
    url = "https://www.wegow.com/api/search/events/"
    parser = DataclassParser(EventSearchResponse)

    def __init__(self, search: SearchParams | None = None):
        self.params = search


class SearchArtist(RequestsEndpoint):
    method = Methods.GET
    url = "https://www.wegow.com/api/search/artists/"
    parser = DataclassParser(ArtistSearchResponse)

    def __init__(self, search: SearchParams | None = None):
        self.params = search


class SearchVenue(RequestsEndpoint):
    method = Methods.GET
    url = "https://www.wegow.com/api/search/venues/"
    parser = DataclassParser(VenueSearchResponse)

    def __init__(self, search: SearchParams | None = None):
        self.params = search


class MediaEndpoint(RequestsEndpoint):
    method = Methods.GET
    url = "https://www.wegow.com/api/media/"
    parser = DataclassParser(MediaEndpointResponse)

    def __init__(self, search: MediaEndpointParams | None = None):
        self.params = search
