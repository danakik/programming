import pytest

from task_5.task_5_2 import amount_of_numbers


@pytest.mark.parametrize('input_param, expected', [(154, 3), (2, 1), (0, 1)])
def test_amount_of_numbers(input_param, expected):
    actual = amount_of_numbers(input_param)
    assert expected == actual
