import os

import pytest

from task_6.task_6_1 import calculate_sum, parity_check


def test_calculate_sum():
    test_file = 'test_numbers.txt'
    numbers = [1, 5, 1]
    with open(test_file, 'w') as file:
        for number in numbers:
            file.write(str(number) + '\n')
    result = calculate_sum(test_file)
    expected_sum = sum(numbers)
    os.remove(test_file)
    assert result == expected_sum


@pytest.mark.parametrize('input_param, expected', [(2, 'Double number'), (9, 'Not a pair number')])
def test_parity_check(input_param, expected):
    actual = parity_check(input_param)
    assert expected == actual
