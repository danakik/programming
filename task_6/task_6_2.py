def read(f_name):
    lines = []
    with open(f_name, 'r') as file:
        for line in file:
            lines.append(line.strip())
    return lines


def modified_line(f_name):
    lines = []
    with open(f_name, 'r') as file:
        for line in file:
            modified = line.replace('Python', 'C')
            lines.append(modified.strip())
    return lines


if __name__ == '__main__':
    f_name = 'learning_python.txt'
    text = read(f_name)
    print("List of lines:")
    for line in text:
        print(line)

    modified = modified_line(f_name)
    for line in modified:
        print(line)
