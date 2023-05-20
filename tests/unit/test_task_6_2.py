import os

import pytest

from task_6.task_6_2 import read, modified_line


def test_read():
    test_file = 'test_read.txt'
    lines = ['In Python you can 1 \
                In Python you can 2 \
                In Python you can 3 \
                In Python you can 4']
    with open(test_file, 'w') as file:
        for line in lines:
            file.write(line + '\n')
    result = read(test_file)
    os.remove(test_file)
    assert result == lines


def test_modified_line():
    test_file = 'test_lines.txt'
    lines = ['I love Python', 'Python is great', 'Python programming']
    with open(test_file, 'w') as file:
        for line in lines:
            file.write(line + '\n')
    result = modified_line(test_file)
    expected = ['I love C', 'C is great', 'C programming']
    os.remove(test_file)
    assert result == expected
