import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


class Triangle:
    def __init__(self, point_1, point_2, point_3):
        self.point1 = point_1
        self.point2 = point_2
        self.point3 = point_3

    def __str__(self):
        return f"Triangle with points: {self.point1}, {self.point2}, {self.point3}"

    def get_side_lengths(self):
        side1 = self.calculate_distance(self.point1, self.point2)
        side2 = self.calculate_distance(self.point2, self.point3)
        side3 = self.calculate_distance(self.point3, self.point1)
        return side1, side2, side3

    def get_square(self):
        side1, side2, side3 = self.get_side_lengths()
        semi_perimeter = (side1 + side2 + side3) / 2
        square = math.sqrt(semi_perimeter * (semi_perimeter - side1) *
                           (semi_perimeter - side2) * (semi_perimeter - side3))
        return square

    def calculate_distance(self, point_1, point_2):
        return math.sqrt((point_2.x - point_1.x) ** 2 + (point_2.y - point_1.y) ** 2)


if __name__ == '__main__':
    point1 = Point(1, 0)
    point2 = Point(3, 2)
    point3 = Point(1, 4)

    triangle = Triangle(point1, point2, point3)
    print(triangle)

    side_lengths = triangle.get_side_lengths()
    print(side_lengths)

    print(triangle.get_square())
