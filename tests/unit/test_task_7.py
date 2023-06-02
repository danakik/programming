import pytest
from task_7.task7 import Point, Triangle


@pytest.fixture
def t_obj():
    point1 = Point(0, 0)
    point2 = Point(3, 0)
    point3 = Point(0, 4)
    return Triangle(point1, point2, point3)


def test_get_side_lengths(t_obj):
    actual = t_obj.get_side_lengths()
    assert actual == (3, 5, 4)


def test_get_square(t_obj):
    actual = t_obj.get_square()
    assert actual == 6
