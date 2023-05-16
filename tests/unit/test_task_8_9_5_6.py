import pytest

from task_8_9.task_8_9_5_6 import get_days_in_month, is_leap_year, input_validation_month, input_validation_year


@pytest.mark.parametrize('input_param, expected', [("january", 31), ("april", 30), ("february", "28 or 29")])
def test_get_days_in_month(input_param, expected):
    actual = get_days_in_month(input_param)
    assert expected == actual


@pytest.mark.parametrize('input_param, expected', [(2020, True), (2015, False)])
def test_is_leap_year(input_param, expected):
    actual = is_leap_year(input_param)
    assert expected == actual


@pytest.mark.parametrize('input_param, expected', [("january", "january")])
def test_input_validation_month(input_param, expected):
    actual = input_validation_month(input_param)
    assert expected == actual


@pytest.mark.parametrize('input_param, expected', [(200, 200)])
def test_input_validation_year(input_param, expected):
    actual = input_validation_year(input_param)
    assert expected == actual