import pytest

from task_8_9.task_8_9_8 import calculator, input_validation_operator


@pytest.mark.parametrize('input_param_1, input_param_2, input_param_3, expected',
                         [(2, 2, '+', 4), (2, 2, '-', 0), (2, 0, '/', None), (2, 2, '/', 1),
                          (2, 2, '*', 4), (2, 2, 'pow', 4), (2, 2, 'mod', 0), (2, 2, 'div', 1)])
def test_calculator(input_param_1, input_param_2, input_param_3, expected):
    actual = calculator(input_param_1, input_param_2, input_param_3)
    assert expected == actual


def test_input_validation_operator_negative(monkeypatch, capsys):
    input_values = ['--', '-']
    monkeypatch.setattr('builtins.input', lambda _: input_values.pop(0))
    input_validation_operator()
    captured = capsys.readouterr()
    assert captured.out == 'No such operator\n'


def test_input_validation_operator(monkeypatch):
    input_values = ['-']
    monkeypatch.setattr('builtins.input', lambda _: input_values.pop(0))
    actual = input_validation_operator()
    assert actual == '-'
