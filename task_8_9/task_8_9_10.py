import re


def input_validation_position(position):
    while not re.match(r'^[a-h][1-8]$', position, re.IGNORECASE):
        print('NONE')
        position = input("Enter the chess position: ")
    return position


def get_square_color(position):
    file = position[0]
    rank = int(position[1])

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
    position_validation = input("Enter the chess position: ")
    position = input_validation_position(position_validation)
    color = get_square_color(position)
    print("The square color is", color)
