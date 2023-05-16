import math as m
from utils import validate_input


def solve_task(num):
    term = (num ** 3) / m.factorial(3 * num - 3)
    series_sum = term

    while abs(term) > 0.0001:
        num += 1
        term = (num ** 3) / m.factorial(3 * num - 3)
        series_sum += term

    return round(series_sum, 4)


if __name__ == '__main__':
    print('Multiparadigm programming languages : Task 5.1')
    print('Danil Mashkin, FI-9119')

    n = validate_input('Enter the number')
    answer = solve_task(n)
    print(answer)
