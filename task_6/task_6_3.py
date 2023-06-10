
def book_filling(f_name):
    with open(f_name, 'a') as file:
        while True:
            name = input("Enter your name (or 'exit' to quit): ")
            if name.lower() == 'exit':
                break
            greeting = f"Hello, {name}! Welcome to the guest book."
            print(greeting)
            file.write(greeting + '\n')


if __name__ == '__main__':
    f_name = 'guest_book.txt'
    book_filling(f_name)


