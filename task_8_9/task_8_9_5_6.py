from utils import validate_input

months = {"january": 31, "february": "28 or 29", "march": 31, "april": 30, "may": 31, "june": 30, "july": 31,
          "august": 31, "september": 30, "october": 31, "november": 30, "december": 31}


def input_validation_month(month):
    while month.lower() not in months:
        print("The entered month does not exist.")
        month = input("Enter the month: ")

    return month.lower()


def input_validation_year(year):
    while year < 0:
        print('year cannot be negative')
        year = validate_input('Enter the year')
    return year


def get_days_in_month(month):
    return months[month]


def is_leap_year(year):
    if year % 4 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    month_validaion = input("Enter the month: ")
    month = input_validation_month(month_validaion)
    days = get_days_in_month(month)
    print(f"The number of days in {month} is {days}")

    year_validaion = validate_input('Enter the year')
    year = input_validation_year(year_validaion)
    if is_leap_year(year):
        print("Leap year.")
    else:
        print("Ordinary year.")