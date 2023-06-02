import pytest

from task_5.task_5_1 import  solve_task


@pytest.mark.parametrize('input_param_1, expected', [(3, 0.0377), (1, 2.371)])
def test_solve_the_task(input_param_1, expected):
    actual = solve_task(input_param_1)
    assert expected == actual
