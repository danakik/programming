print('Multiparadigm programming languages : Task 2')
print('Danil Mashkin, FI-9119')


def validate_input(var_name):
    while True:
        try:
            return int(input('Add the value {}: '.format(var_name)))
        except ValueError:
            print('Please enter a number')


x = validate_input('x')
y = validate_input('y')
z = validate_input('z')

result = (((z - 23.1) * ((2 ** x) + 2.2)) / (y - 21.1)) - 3.2
print(round(result, 5))
