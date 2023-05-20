from utils import validate_input_v2


def calculate_sum(f_name):
    total_sum = 0
    with open(f_name, 'r') as file:
        for line in file:
            number = float(line.strip())
            total_sum += number
    return total_sum


def write_sum(total_sum):
    with open('sum_numbers.txt', 'w') as file:
        file.write(str(total_sum))


def parity_check(n):
    if n % 2 == 0:
        check = "Double number"
    else:
        check = "Not a pair number"
    return check


def write_check(check):
    with open('check.txt', 'w') as file:
        file.write(str(check))


if __name__ == '__main__':

    f_name = 'numbers.txt'
    total_sum = calculate_sum(f_name)
    print("Sum of numbers:", total_sum)
    write_sum(total_sum)

    num = validate_input_v2("Enet nubers")
    check = parity_check(num)
    write_check(check)

