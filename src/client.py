from typing import Iterator

import requests
from api_consumer.requests import RequestsClient

from endpoints import EventFeedEndpoint
from endpoints import MediaEndpoint
from endpoints import RetrieveArtist
from endpoints import RetrieveEvent
from endpoints import RetrieveVenue
from endpoints import SearchArtist
from endpoints import SearchEvent
from endpoints import SearchVenue
from models.common import SearchParams
from models.event import Event
from models.event import EventFeedResponse
from models.full_artist import FullArtist
from models.full_event import FullEvent
from models.full_venue import FullVenue
from models.media import MediaEndpointParams
from models.venue import Venue


class WegowClient(RequestsClient):
    def __init__(self):
        self.session = requests.Session()

    def event_feed(self, page: int | None = None) -> EventFeedResponse:
        return self._perform_request(EventFeedEndpoint(page))

    def get_events(self) -> Iterator[Event]:
        """Returns an iterator containing all concerts"""
        next_page = None
        while True:
            response = self.event_feed(page=next_page)
            yield from response.events
            next_page = response.next_page
            if next_page is None:
                break

    def get_event(self, event_id: int | str) -> FullEvent:
        endpoint = RetrieveEvent(event_id=event_id)
        return self._perform_request(endpoint)

    def get_venue(self, venue_id: int | str) -> FullVenue:
        endpoint = RetrieveVenue(venue_id=venue_id)
        return self._perform_request(endpoint)

    def get_artist(self, artist_id: int | str) -> FullArtist:
        endpoint = RetrieveArtist(artist_id=artist_id)
        return self._perform_request(endpoint)

    def search_events(self, params: SearchParams):
        endpoint = SearchEvent(params)
        return self._perform_request(endpoint)

    def search_artists(self, params: SearchParams):
        endpoint = SearchArtist(params)
        return self._perform_request(endpoint)

    def search_venues(self, params: SearchParams) -> list[Venue]:
        endpoint = SearchVenue(params)
        response = self._perform_request(endpoint)
        return response.venues

    def get_media(self, event_id: int | str):
        endpoint = MediaEndpoint(MediaEndpointParams(event=event_id))
        return self._perform_request(endpoint)
