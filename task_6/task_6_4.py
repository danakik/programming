import re


def count_the():
    count = 0
    with open('in_the_home.txt', 'r') as file:
        for line_number, line in enumerate(file, start=1):
            matches = re.findall(r'\bthe\b', line, re.IGNORECASE)
            count += len(matches)
    return count


if __name__ == '__main__':
    result = count_the()
    print("Number of occurrences:", result)
