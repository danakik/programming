import pytest

from task_8_9.task_8_9_10 import get_square_color, input_validation_position


@pytest.mark.parametrize('input_param, expected', [('c4', 'white'), ('a1', 'black'), ('b1', 'white'), ('f2', 'black')])
def test_get_square_color(input_param, expected):
    actual = get_square_color(input_param)
    assert expected == actual


@pytest.mark.parametrize('input_param, expected', [('c4', 'c4')])
def test_input_validation_position(input_param, expected):
    actual = input_validation_position(input_param)
    assert expected == actual
