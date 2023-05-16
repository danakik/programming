import random
import re

choice_dict = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}


def beginning_of_the_game():
    play_again = ''
    while play_again.lower() != 'no':
        yes_no = r'^(yes|no)$'
        player_choice = get_player_choice()
        play_game(player_choice)

        play_again = input("Do you want to play again? (yes/no): ")
        while not re.match(yes_no, play_again, re.IGNORECASE):
            print('The entered answer does not exist')
            play_again = input("Do you want to play again? (yes/no): ")
    print("Thanks for playing!")


def play_game(player_choice):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    print(f"Your choice: {player_choice}")
    print(f"Computer's choice: {computer_choice}")
    player_choice_lower = player_choice.lower()

    if player_choice == computer_choice:
        print("It's a draw!")
    elif computer_choice in choice_dict[player_choice_lower]:
        print("You win!")
    else:
        print("Computer wins!")


def get_player_choice():
    items = r'^(rock|paper|scissors)$'
    while True:
        choice = input("Choose rock, paper, or scissors: ")
        if re.match(items, choice, re.IGNORECASE):
            return choice
        print("Invalid choice. Please try again.")


if __name__ == '__main__':
    print("Rock, Paper, Scissors Game")
    beginning_of_the_game()
