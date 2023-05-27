import re


def input_validation_position():
    location = input('Enter the chess position: ')
    while not re.match(r'^[a-h][1-8]$', location, re.IGNORECASE):
        print('No such cell')
        location = input('Enter the chess position: ')
    return location


def get_square_color(location):
    file = location[0]
    rank = int(location[1])

    if file in ['a', 'c', 'e', 'g']:
        if rank % 2 == 0:
            return 'white'
        else:
            return 'black'
    else:
        if rank % 2 == 0:
            return 'black'
        else:
            return 'white'


if __name__ == '__main__':
    position = input_validation_position()
    print(f'The square color is {get_square_color(position)}')
