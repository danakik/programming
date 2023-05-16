from utils import validate_input_v2
import re


def input_validation_operator(operator):
    pattern = r'^(\+|-|/|mod|pow|div|\*)$'
    while not re.match(pattern, operator, re.IGNORECASE):
        print('No such operator')
        operator = input("Enter the operator (+, -, /, *, mod, pow, div): ")
    return operator


def calculator(num1, num2, operator):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '/':
        if num2 == 0:
            result = "Division by zero!"
        else:
            result = num1 / num2
    elif operator == '*':
        result = num1 * num2
    elif operator == 'mod':
        result = num1 % num2
    elif operator == 'pow':
        result = num1 ** num2
    elif operator == 'div':
        result = num1 // num2
    return result


if __name__ == '__main__':
    num1 = validate_input_v2("Enter the first number")
    num2 = validate_input_v2("Enter the second number")
    operator_validation = input("Enter the operator (+, -, /, *, mod, pow, div): ")
    operator = input_validation_operator(operator_validation)
    result = calculator(num1, num2, operator)
    print("Result:", result)
