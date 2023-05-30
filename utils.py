def validate_input(var_name):
    while True:
        try:
            return int(input('{}: '.format(var_name)))
        except ValueError:
            print('Please enter a number(int type)')


def validate_input_v2(var_name):
    while True:
        try:
            return int(input('{}: '.format(var_name)))
        except ValueError:
            print('Please enter a number')

