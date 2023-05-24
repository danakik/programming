import pytest

from task_8_9.task_8_9_5_6 import is_leap_year, input_validation_month, input_validation_year


@pytest.mark.parametrize('input_param, expected', [(2020, 'Leap'), (2015, 'Ordinary')])
def test_is_leap_year(input_param, expected):
    actual = is_leap_year(input_param)
    assert expected == actual


@pytest.mark.parametrize('input_param, expected', [("january", "january")])
def test_input_validation_month(input_param, expected):
    actual = input_validation_month(input_param)
    assert expected == actual


@pytest.mark.parametrize('input_param, expected', [(200, 200)])
def test_input_validation_year(input_param, expected):
    actual = input_validation_year()
    assert expected == actual


def test_input_validation_year_negative(monkeypatch, capsys):
    input_values = ['-2023', '2023']
    monkeypatch.setattr('builtins.input', lambda _: input_values.pop(0))
    input_validation_year()
    captured = capsys.readouterr()
    assert captured.out == 'year cannot be negative\n'
