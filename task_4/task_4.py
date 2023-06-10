from utils import validate_input


def check_simple(num):
    if num < 2:
        return False
    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            return False
    return True


def first_five_simple_numbers(k):
    simple_numbers = []
    while len(simple_numbers) < 5:
        k += 1
        if check_simple(k):
            simple_numbers.append(k)
    return simple_numbers


if __name__ == '__main__':
    print('Multiparadigm programming languages : Task 4')
    print('Danil Mashkin, FI-9119')

    n = validate_input('Enter the number')
    ff = first_five_simple_numbers(n)
    print(ff)
