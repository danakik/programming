import pytest
import os
import re
from task_6.task_6_4 import count_the


@pytest.fixture
def test_file():
    test_file_path = 'in_the_home.txt'
    lines = ['The cat is on the mat.', 'There are three birds in the tree.', 'The sun is shining.']
    with open(test_file_path, 'w') as file:
        for line in lines:
            file.write(line + '\n')
    yield test_file_path
    os.remove(test_file_path)


def test_count_the(test_file):
    expected_count = 4
    result = count_the()
    assert result == expected_count
