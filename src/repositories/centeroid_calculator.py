import math


class CentroidCalculator:
    def __init__(self, distance_type: str = "euclidean"):
        self.distance_type = distance_type

    def calculate_centeroid(self, list_of_points: list[tuple[float, float]]):
        if self.distance_type == "euclidean":
            return self._calculate_euclidean_centeroid(list_of_points)
        else:
            raise ValueError("Unknown distance type")

    def _calculate_euclidean_centeroid(self, list_of_points: list[tuple[float, float]]):
        x = [point[0] for point in list_of_points]
        y = [point[1] for point in list_of_points]
        return (sum(x) / len(x), sum(y) / len(y))

    def distance_between_points(
        self, point1: tuple[float, float], point2: tuple[float, float]
    ) -> float:
        if self.distance_type == "euclidean":
            return self._euclidean_distance(point1, point2)
        else:
            raise ValueError("Unknown distance type")

    def _euclidean_distance(
        self, point1: tuple[float, float], point2: tuple[float, float]
    ):
        return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
