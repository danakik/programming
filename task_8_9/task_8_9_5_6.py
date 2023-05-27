from utils import validate_input

months = {"january": 31, "february": "28 or 29", "march": 31, "april": 30, "may": 31, "june": 30, "july": 31,
          "august": 31, "september": 30, "october": 31, "november": 30, "december": 31}


def input_validation_month():
    month = input("Enter the month: ")
    while month.lower() not in months:
        print("The entered month does not exist")
        month = input("Enter the month: ")
    return months[month.lower()], month


def input_validation_year():
    while True:
        year = validate_input('Enter the year')
        if year >= 0:
            return year
        print('year cannot be negative')


def is_leap_year(year):
    return 'Ordinary' if year % 4 else 'Leap'


def main():
    days, month = input_validation_month()
    print(f'The number of days in {month} is {days}')

    year = input_validation_year()
    print(f'{is_leap_year(year)} year')


if __name__ == '__main__':
    main()
