import pytest

from task_4.task_4 import first_five_simple_numbers, check_simple


def test_check_simple_less_two():
    expected = False
    actual = check_simple(1)
    assert expected == actual


def test_check_simple_simple_value():
    expected = True
    actual = check_simple(5)
    assert expected == actual


def test_check_simple_not_simple_value():
    expected = False
    actual = check_simple(6)
    assert expected == actual


@pytest.mark.parametrize('input_param, expected', [(1, [2, 3, 5, 7, 11]), (20, [23, 29, 31, 37, 41])])
def test_first_five_simple_numbers(input_param, expected):
    actual = first_five_simple_numbers(input_param)
    assert expected == actual
