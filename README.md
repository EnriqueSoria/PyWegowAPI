# PyWegowAPI

A client for the public, undocumented, Wegow API

```python
>>> from client import WegowClient
>>> client = WegowClient()
>>> client.search_venues({"query": "repvblicca"})
[
    Venue(
        id=132176,
        name="Sala Repvblicca",
        image_url="https://cdn.wegow.com/media/venues/sala-repvblicca/sala-repvblicca-1580916864.0651102.jpg",
        permalink="https://www.wegow.com/es/recintos/sala-republica",
        longitude=-0.427002300000026,
        latitude=39.4725568,
        thumbnails="venues/sala-repvblicca/sala-repvblicca-1580916864.0651102.jpg",
    ),
    Venue(
        id=166895,
        name="Sala Repvblicca 2",
        image_url="https://cdn.wegow.com/media/venues/sala-repvblicca-2/sala-repvblicca-2-1643107791.3883321.jpg",
        permalink="https://www.wegow.com/es/nr/recintos/sala-repvblicca-2",
        longitude=-0.4270267,
        latitude=39.472479,
        thumbnails="venues/sala-repvblicca-2/sala-repvblicca-2-1643107791.3883321.jpg",
    ),
]
```


```python
>>> client.get_venue(results[0].id)
FullVenue(
    id=132176,
    name="Sala Repvblicca",
    image_url="https://cdn.wegow.com/media/venues/sala-repvblicca/sala-repvblicca-1580916864.0651102.jpg",
    permalink="https://www.wegow.com/es/recintos/sala-republica",
    longitude=-0.427002300000026,
    latitude=39.4725568,
    thumbnails="venues/sala-repvblicca/sala-repvblicca-1580916864.0651102.jpg",
    city=City(
        id=2513811,
        name="Mislata",
        administrative_division="Valencia",
        country="España",
        iso_code="ES",
        index=False,
        timezone="Europe/Madrid",
    ),
    enabled=True,
    slug="sala-republica",
    user=User(following=False),
    followers_count=550,
    events_count=16,
    index=True,
    description="Sala Republica, la sala de conciertos de referencia, más grande y de calidad de toda Valencia.\r\nPodrás ver a tus artistas nacionales e internacionales favoritos.",
    address="Pol. Industrial Mislata, Carrer Baix Vinalopó, 2, 46920 Mislata, Valencia",
    directions="Metro: Mislata - Almassil o Faitanar (líneas 3, 5 y 9)",
    facebook_pixel_js="",
    google_pixel_js="",
    adwords="",
    companies=[],
    canonical="https://www.wegow.com/es/recintos/sala-republica",
    links=[
        {"id": 185, "type": 1, "url": "https://www.facebook.com/repvbliccaoficial/"},
        {"id": 186, "type": 0, "url": "http://www.republicca.com"},
    ],
)

```

Built with ♥ using [python-api-consumer](https://github.com/EnriqueSoria/python-api-consumer)