from utils import validate_input


def amount_of_numbers(num):
    if num == 0:
        return 1

    amount = 0
    while num:
        amount += 1
        num //= 10
    return amount


if __name__ == '__main__':
    print('Multiparadigm programming languages : Task 5.2')
    print('Danil Mashkin, FI-9119')
    NUM = abs(validate_input('Enter the number'))
    COUNT = amount_of_numbers(NUM)
    print(COUNT)
