import pytest

from task_8_9.task_8_9_8 import calculator, input_validation_operator


@pytest.mark.parametrize('input_param_1, input_param_2, input_param_3, expected',
                         [(2, 2, '+', 4), (5, 2, '-', 3), (2, 0, '/', "Division by zero!"), (6, 2, '/', 3),
                          (5, 2, '*', 10), (5, 2, 'pow', 25), (4, 2, 'mod', 0), (7, 3, 'div', 2)])
def test_calculator(input_param_1, input_param_2, input_param_3, expected):
    actual = calculator(input_param_1, input_param_2, input_param_3)
    assert expected == actual


@pytest.mark.parametrize('input_param, expected', [("mod", "mod")])
def test_input_validation_operator(input_param, expected):
    actual = input_validation_operator(input_param)
    assert expected == actual
