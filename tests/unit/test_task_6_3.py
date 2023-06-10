import pytest
from unittest.mock import patch
import os

from task_6.task_6_3 import book_filling


@pytest.fixture
def test_file():
    test_file_path = 'test_guest_book.txt'
    yield test_file_path
    os.remove(test_file_path)


@patch('builtins.input', side_effect=['Den', 'Bob', 'exit'])
def test_book_filling(mock_input, capsys, test_file):
    expected_lines = ['Hello, Den! Welcome to the guest book.',
                      'Hello, Bob! Welcome to the guest book.']

    book_filling(test_file)

    captured = capsys.readouterr()
    output = captured.out.strip()

    with open(test_file, 'r') as file:
        result_lines = [line.strip() for line in file]

    assert output == '\n'.join(expected_lines)
    assert result_lines == expected_lines
