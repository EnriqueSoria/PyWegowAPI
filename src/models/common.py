from dataclasses import dataclass


@dataclass
class SearchParams:
    query: str
    page: int = 1
    page_size: int = 20
    region: str = "es-es"
    mongo: bool = True
