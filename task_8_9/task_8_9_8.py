import re
from utils import validate_input


def input_validation_operator():
    pattern = r'^(\+|-|/|mod|pow|div|\*)$'
    operator = input('Enter the operator (+, -, /, *, mod, pow, div): ')
    while not re.match(pattern, operator, re.IGNORECASE):
        print('No such operator')
        operator = input('Enter the operator (+, -, /, *, mod, pow, div): ')
    return operator


def calculator(num_1, num_2, operator):
    answer = None
    if operator == '+':
        answer = num_1 + num_2
    elif operator == '-':
        answer = num_1 - num_2
    elif operator == '/':
        if num_2:
            answer = num_1 / num_2
    elif operator == '*':
        answer = num_1 * num_2
    elif operator == 'mod':
        answer = num_1 % num_2
    elif operator == 'pow':
        answer = num_1 ** num_2
    elif operator == 'div':
        answer = num_1 // num_2
    return answer


if __name__ == '__main__':
    num1 = validate_input('Enter the first number', float)
    num2 = validate_input('Enter the second number', float)
    symbol = input_validation_operator()
    result = calculator(num1, num2, symbol)
    print('Result:', result if result is not None else 'Division by zero!')
