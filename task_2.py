import utils

print('Multiparadigm programming languages : Task 2')
print('Danil Mashkin, FI-9119')

x = utils.validate_input('x')
y = utils.validate_input('y')
z = utils.validate_input('z')

result = (((z - 23.1) * ((2 ** x) + 2.2)) / (y - 21.1)) - 3.2
print(round(result, 5))
