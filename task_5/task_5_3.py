from utils import validate_input


def square_root(num):
    while num < 0:
        num = validate_input('Enter a positive number')
    x_0 = num
    accuracy = 0.0001
    while True:
        next_x = 0.5 * (x_0 + num / x_0)
        if abs(next_x - x_0) < accuracy:
            return round(next_x, 4)
        x_0 = next_x


if __name__ == '__main__':
    n = validate_input('Enter the number')
    result = square_root(n)
    print(result)
