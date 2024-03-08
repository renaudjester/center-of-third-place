from functools import lru_cache
from typing import cast

from dependencies import Injector, value
from repositories.centeroid_calculator import CentroidCalculator
from repositories.google_maps_links_converter import (
    GoogleMapsLinksConverter,
    GoogleMapsLinksConverterConnection,
)
from repositories.mongodb import MongoDB, MongoDBConnection


class Container(Injector):
    centroid_calculator = cast(CentroidCalculator, CentroidCalculator)
    google_maps_links_converter = cast(
        GoogleMapsLinksConverter, GoogleMapsLinksConverter
    )
    mongodb = cast(MongoDB, MongoDB)

    @value
    @lru_cache
    def google_maps_links_converter_connection() -> GoogleMapsLinksConverterConnection:
        return GoogleMapsLinksConverterConnection()

    @value
    @lru_cache
    def mongodb_connection() -> MongoDBConnection:
        return MongoDBConnection("localhost", 27017, "thirdplace")


def init_container():
    pass


def shutdown_container():
    Container.google_maps_links_converter.close()
    Container.mongodb.close()
