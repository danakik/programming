from math import sqrt


class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        return f"({self._x}, {self._y})"


class Triangle:
    def __init__(self, point_1, point_2, point_3):
        self._point1 = point_1
        self._point2 = point_2
        self._point3 = point_3

    def __str__(self):
        return f"Triangle with points: {self._point1}, {self._point2}, {self._point3}"

    def get_side_lengths(self):
        side1 = self._calculate_distance(self._point1, self._point2)
        side2 = self._calculate_distance(self._point2, self._point3)
        side3 = self._calculate_distance(self._point3, self._point1)
        return side1, side2, side3

    def get_square(self):
        side1, side2, side3 = self.get_side_lengths()
        semi_perimeter = (side1 + side2 + side3) / 2
        square = sqrt(semi_perimeter * (semi_perimeter - side1) *
                      (semi_perimeter - side2) * (semi_perimeter - side3))
        return square

    @staticmethod
    def _calculate_distance(point_1, point_2):
        return sqrt((point_2._x - point_1._x) ** 2 + (point_2._y - point_1._y) ** 2)


if __name__ == '__main__':
    point1 = Point(1, 0)
    point2 = Point(3, 2)
    point3 = Point(1, 4)

    triangle = Triangle(point1, point2, point3)
    print(triangle)

    side_lengths = triangle.get_side_lengths()
    print(side_lengths)

    print(triangle.get_square())
