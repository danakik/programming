def validate_input(var_name, cast_fnc=int):
    while True:
        try:
            return cast_fnc(input(f'{var_name}: '))
        except ValueError:
            print('Please enter a number(int type)')
