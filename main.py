from centeroid_calculator import CentroidCalculator
from google_maps_links_converter import (
    GoogleMapsLinksConverter,
    GoogleMapsLinksConverterConnection,
)

if __name__ == "__main__":
    # let's get the user to input the points
    points = []
    while True:
        point = input(
            "Enter a point (lat, lon) in a format'lat, lon' or 'done' to finish: "
        )
        if point == "done":
            break
        x, y = point.split(", ")
        points.append((float(x), float(y)))
    with GoogleMapsLinksConverterConnection() as connection:
        while True:
            link = input("Enter a google maps link or 'done' to finish: ")
            if link == "done":
                break
            converter = GoogleMapsLinksConverter(connection)
            points.append(converter.get_lat_lon_from_link(link))
            print(
                f"The latitude and longitude of the link is {converter.get_lat_lon_from_link(link)}"
            )
    if not points:
        print("No points were entered")
    else:
        centroid_calculator = CentroidCalculator()
        print(
            f"The centroid of the points is {centroid_calculator.calculate_centeroid(points)}"
        )
