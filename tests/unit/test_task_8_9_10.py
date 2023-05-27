import pytest

from task_8_9.task_8_9_10 import get_square_color, input_validation_position


@pytest.mark.parametrize('input_param, expected', [('a2', 'white'), ('a1', 'black')])
def test_get_square_color(input_param, expected):
    actual = get_square_color(input_param)
    assert expected == actual


def test_input_validation_position_negative(monkeypatch, capsys):
    input_values = ['v5', 'a1']
    monkeypatch.setattr('builtins.input', lambda _: input_values.pop(0))
    input_validation_position()
    captured = capsys.readouterr()
    assert captured.out == 'No such cell\n'


def test_input_validation_position(monkeypatch):
    input_values = ['a1']
    monkeypatch.setattr('builtins.input', lambda _: input_values.pop(0))
    actual = input_validation_position()
    assert actual == 'a1'
