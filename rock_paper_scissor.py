import random

def get_player_choice():
    choice = input("Choose rock, paper, or scissors: ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        choice = input("Choose rock, paper, or scissors: ").lower()
    return choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        return "You win! {} beats {}.".format(player_choice, computer_choice)
    else:
        return "Computer wins! {} beats {}.".format(computer_choice, player_choice)

def play_game():
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    print("You chose:", player_choice)
    print("Computer chose:", computer_choice)
    print(determine_winner(player_choice, computer_choice))

if __name__ == "__main__":
    play_game()
