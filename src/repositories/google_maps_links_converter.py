import requests


class GoogleMapsLinksConverterConnection:
    def __init__(self) -> None:
        self.session = requests.Session()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.session.close()


class GoogleMapsLinksConverter:
    def __init__(
        self, google_maps_links_converter_connection: GoogleMapsLinksConverterConnection
    ):
        self.google_maps_links_converter_connection = (
            google_maps_links_converter_connection
        )

    def from_short_to_long_url(self, link: str) -> str:
        return self.google_maps_links_converter_connection.session.head(
            link, allow_redirects=True
        ).url

    def get_lat_lon_from_long_link(self, link: str) -> list[float]:
        break_down_link = link.split("data=")[-1].split("?")[0]
        lat = float(
            [elmt for elmt in break_down_link.split("!") if elmt.startswith("3d")][
                0
            ].replace("3d", "")
        )
        lon = float(
            [elmt for elmt in break_down_link.split("!") if elmt.startswith("4d")][
                0
            ].replace("4d", "")
        )
        return [lat, lon]

    def get_lat_lon_from_link(self, link: str) -> list[float]:
        return self.get_lat_lon_from_long_link(
            self.from_short_to_long_url(link) if len(link) < 50 else link
        )

    def close(self):
        self.google_maps_links_converter_connection.session.close()
