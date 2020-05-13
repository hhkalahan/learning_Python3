#!/usr/bin/python3

def intro():
    print('*' * 50)
    print('*', ' ' * 46, '*')
    print('*', '      Welcome to Rock Paper Scissors', ' ' * 9, '*')
    print('*', ' ' * 10, 'Lizard Spock GAME.', ' ' * 16, '*')
    print('*', ' ' * 15, "ENJOY!!!", ' ' * 21, '*')
    print('*' * 50)
    print(' ')
    print(' ')


def game_rules():
    print("RULES:\n")
    print("Scissors cuts Paper, Scissors decapitates Lizard, Paper covers Rock, "
          "\nLizard eats Paper, Rock crushes Lizard, Paper disproves Spock, "
          "\nLizard poisons Spock, Spock vaporizes Rock, Spock smashes Scissors, "
          "\nRock crushes Scissors.")
    print('    ')
    print('\tEnter `quit` to exit.\n')
    print(' ')


def main():
    import random

    comp_score = 0
    user_score = 0
    tries = int(input("How many rounds you want to play?\n$: "))
    print('\t     Please choose your weapon!!!')

    for i in range(tries):
        user_choice = input("Rock, Paper, Scissors, Lizard, Spock?\n$: ").lower()
        user_choice.lower()

        stuffs = (['rock', 'paper', 'scissors', 'lizard', 'spock'])
        stuff = random.choice(stuffs)
        comp_choice = stuff

        if user_choice == 'quit':
            print(f"You have selected {user_choice.title()}")
            print("\nClosing the game...")
        else:
            if user_choice == comp_choice:
                print(f"\nYou have selected {user_choice.title()}")
                print(f"Computer choice is {comp_choice.title()}")
                print(f"That is a draw.\n")
                print(f"\t###> The Score is: <###\n\t   Human:{user_score}    AI:{comp_score}\n")
            elif user_choice == 'rock' and comp_choice == 'scissors':
                print(f"\nYou have selected {user_choice.title()}")
                print(f"Computer choice is {comp_choice.title()}")
                print("Rock beats scissors! You WIN!\n")
                user_score += 1
                print(f"\t###> The Score is: <###\n\t     Human:{user_score}    AI:{comp_score}\n")
            elif user_choice == 'scissors' and comp_choice == 'rock':
                print(f"\nYou have selected {user_choice.title()}")
                print(f"Computer choice is {comp_choice.title()}")
                print("Rock beats scissors! CPU WIN\n")
                comp_score += 1
                print(f"\t###> The Score is: <###\n\t     Human:{user_score}    AI:{comp_score}\n")
            elif user_choice == 'rock' and comp_choice == 'paper':
                print(f"\nYou have selected {user_choice.title()}")
                print(f"Computer choice is {comp_choice.title()}")
                print("Paper beats rock! CPU WIN!\n")
                comp_score += 1
                print(f"\t###> The Score is: <###\n\t     Human:{user_score}    AI:{comp_score}\n")
            elif user_choice == 'paper' and comp_choice == 'rock':
                print(f"\nYou have selected {user_choice.title()}")
                print(f"Computer choice is {comp_choice.title()}")
                print("Paper beats rock! You WIN!\n")
                user_score += 1
                print(f"\t###> The Score is: <###\n\t     Human:{user_score}    AI:{comp_score}\n")
            elif user_choice == 'paper' and comp_choice == 'scissors':
                print(f"\nYou have selected {user_choice.title()}")
                print(f"Computer choice is {comp_choice.title()}")
                print("Scissors beats paper! CPU WIN!\n")
                comp_score += 1
                print(f"\t###> The Score is: <###\n\t     Human:{user_score}    AI:{comp_score}\n")
            elif user_choice == 'scissors' and comp_choice == 'paper':
                print(f"\nYou have selected {user_choice.title()}")
                print(f"Computer choice is {comp_choice.title()}")
                print("Scissors beats paper! You WIN!\n")
                user_score += 1
                print(f"\t###> The Score is: <###\n\t     Human:{user_score}    AI:{comp_score}\n")
            elif user_choice == 'scissors' and comp_choice == 'lizard':
                print(f"\nYou have selected {user_choice.title()}")
                print(f"Computer choice is {comp_choice.title()}")
                print("Scissors beats lizard! You WIN!\n")
                user_score += 1
            elif user_choice == 'lizard' and comp_choice == 'paper':
                print(f"\nYou have selected {user_choice.title()}")
                print(f"Computer choice is {comp_choice.title()}")
                print("Lizard eats paper! You WIN!\n")
                user_score += 1
            elif user_choice == 'rock' and comp_choice == 'lizard':
                print(f"\nYou have selected {user_choice.title()}")
                print(f"Computer choice is {comp_choice.title()}")
                print("Rock crushes lizard! You WIN!\n")
                user_score += 1
            elif user_choice == 'paper' and comp_choice == 'spock':
                print(f"\nYou have selected {user_choice.title()}")
                print(f"Computer choice is {comp_choice.title()}")
                print("Paper disproves Spock! You WIN!\n")
                user_score += 1
            elif user_choice == 'lizard' and comp_choice == 'spock':
                print(f"\nYou have selected {user_choice.title()}")
                print(f"Computer choice is {comp_choice.title()}")
                print("Lizard poison Spock! You WIN!\n")
                user_score += 1
            elif user_choice == 'spock' and comp_choice == 'rock':
                print(f"\nYou have selected {user_choice.title()}")
                print(f"Computer choice is {comp_choice.title()}")
                print("Spock vaporizes rock! You WIN!\n")
                user_score += 1
            elif user_choice == 'spock' and comp_choice == 'scissors':
                print(f"\nYou have selected {user_choice.title()}")
                print(f"Computer choice is {comp_choice.title()}")
                print("Spock smashes scissors! You WIN!\n")
                user_score += 1
            elif user_choice == 'lizard' and comp_choice == 'scissors':
                print(f"\nYou have selected {user_choice.title()}")
                print(f"Computer choice is {comp_choice.title()}")
                print("Scissors beats lizard! CPU WIN!\n")
                user_score += 1
            elif user_choice == 'paper' and comp_choice == 'lizard':
                print(f"\nYou have selected {user_choice.title()}")
                print(f"Computer choice is {comp_choice.title()}")
                print("Lizard eats paper! CPU WIN!\n")
                user_score += 1
            elif user_choice == 'lizard' and comp_choice == 'rock':
                print(f"\nYou have selected {user_choice.title()}")
                print(f"Computer choice is {comp_choice.title()}")
                print("Rock crushes lizard! CPU WIN!\n")
                user_score += 1
            elif user_choice == 'spock' and comp_choice == 'paper':
                print(f"\nYou have selected {user_choice.title()}")
                print(f"Computer choice is {comp_choice.title()}")
                print("Paper disproves Spock! CPU WIN!\n")
                user_score += 1
            elif user_choice == 'spock' and comp_choice == 'lizard':
                print(f"\nYou have selected {user_choice.title()}")
                print(f"Computer choice is {comp_choice.title()}")
                print("Lizard poison Spock! CPU WIN!\n")
                user_score += 1
            elif user_choice == 'rock' and comp_choice == 'spock':
                print(f"\nYou have selected {user_choice.title()}")
                print(f"Computer choice is {comp_choice.title()}")
                print("Spock vaporizes rock! CPU WIN!\n")
                comp_score += 1
            elif user_choice == 'scissors' and comp_choice == 'spock':
                print(f"\nYou have selected {user_choice.title()}")
                print(f"Computer choice is {comp_choice.title()}")
                print("Spock smashes scissors! CPU WIN!\n")
                comp_score += 1
            elif user_choice == 'scissors' and comp_choice == 'lizard':
                print(f"\nYou have selected {user_choice.title()}")
                print(f"Computer choice is {comp_choice.title()}")
                print("Scissors decapitates lizard! You WIN!\n")
                user_score += 1
            elif user_choice == 'lizard' and comp_choice == 'paper':
                print(f"\nYou have selected {user_choice.title()}")
                print(f"Computer choice is {comp_choice.title()}")
                print("Lizard eats paper! You WIN!\n")
                user_score += 1
            elif user_choice == 'rock' and comp_choice == 'lizard':
                print(f"\nYou have selected {user_choice.title()}")
                print(f"Computer choice is {comp_choice.title()}")
                print("Rock crushes lizard! You WIN!\n")
                user_score += 1
            elif user_choice == 'paper' and comp_choice == 'spock':
                print(f"\nYou have selected {user_choice.title()}")
                print(f"Computer choice is {comp_choice.title()}")
                print("Paper disproves Spock! You WIN!\n")
                user_score += 1
            elif user_choice == 'lizard' and comp_choice == 'spock':
                print(f"\nYou have selected {user_choice.title()}")
                print(f"Computer choice is {comp_choice.title()}")
                print("Lizard poison Spock! You WIN!\n")
                user_score += 1
            elif user_choice == 'spock' and comp_choice == 'rock':
                print(f"\nYou have selected {user_choice.title()}")
                print(f"Computer choice is {comp_choice.title()}")
                print("Spock vaporizes rock! You WIN!\n")
                user_score += 1
            elif user_choice == 'spock' and comp_choice == 'scissors':
                print(f"\nYou have selected {user_choice.title()}")
                print(f"Computer choice is {comp_choice.title()}")
                print("Spock smashes scissors! You WIN!\n")
                user_score += 1
            else:
                print("Ops wrong entry. Try again.")
        print(f"\t###> The Score is: <###\n\t   Human:{user_score}    AI:{comp_score}\n")


intro()
game_rules()
main()
