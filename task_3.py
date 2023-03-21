import math as m
import utils

print('Multiparadigm programming languages : Task 3')
print('Danil Mashkin, FI-9119')

x = y = None
while x == y:
    print('X should not be equal Y')
    x = utils.validate_input('x')
    y = utils.validate_input('y')

result = (1 / ((x ** 3) - (y ** 3))) - m.sqrt(2 * x)
print(round(result, 5))
