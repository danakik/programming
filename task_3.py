import math as m

print('Multiparadigm programming languages : Task 3')
print('Danil Mashkin, FI-9119')


def validate_input(var_name):
    while True:
        try:
            return int(input('Input {}: '.format(var_name)))
        except ValueError:
            print('Please enter a number')


x = y = None

while x == y:
    print('X should not be equal Y')
    x = validate_input('x')
    y = validate_input('y')

result = (1 / ((x ** 3) - (y ** 3))) - m.sqrt(2 * x)
print(round(result, 5))
