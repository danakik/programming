import pytest

from task_5.task_5_3 import square_root


@pytest.mark.parametrize('input_param, expected', [(2, 1.4142), (9, 3)])
def test_square_root(input_param, expected):
    actual = square_root(input_param)
    assert expected == actual
