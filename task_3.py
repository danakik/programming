import math as m
import utils

print('Multiparadigm programming languages : Task 3')
print('Danil Mashkin, FI-9119')

X = Y = None
while X == Y:
    print('X should not be equal Y')
    X = utils.validate_input('x')
    Y = utils.validate_input('y')

result = (1 / ((X ** 3) - (Y ** 3))) - m.sqrt(2 * X)
print(round(result, 5))
