#!/usr/bin/python3

def intro():
    print('*' * 50)
    print('*', ' ' * 46, '*')
    print('*', '   Welcome to Rock,Paper,Scissors GAME!!!', ' ' * 4, '*')
    print('*', ' ' * 15, "ENJOY!!!", ' ' * 21, '*')
    print('*', ' ' * 46, '*')
    print('*' * 50)
    print(' ')
    print(' ')
    print('    ')
    print('\tEnter `quit` to exit.\n')
    print('\tPlease choose your weapon!!!')
    print(' ')


def main():

    import random

    comp_score = 0
    user_score = 0
    tries = int(input("How many rounds you want to play?\n$: "))

    for i in range(tries):
        user_choice = input("Rock, Paper or Scissors?\n$: ").lower()
        user_choice.lower()

        stuffs = (['rock', 'paper', 'scissors'])
        stuff = random.choice(stuffs)
        comp_choice = stuff

        if user_choice == 'quit':
            print(f"You have selected {user_choice.title()}")
            print("\nClosing the game...")
            # break
        else:
            if user_choice == comp_choice:
                print(f"\nYou have selected {user_choice.title()}")
                print(f"Computer choice is {comp_choice.title()}")
                print(f"That is a draw.\n")
                print(f"\t###> The Score is: <###\n\t   Human:{user_score}    AI:{comp_score}\n")
            elif user_choice == 'rock' and comp_choice == 'scissors':
                print(f"\nYou have selected {user_choice.title()}")
                print(f"Computer choice is {comp_choice.title()}")
                print("Rock beats scissors You WIN!\n")
                user_score += 1
                print(f"\t###> The Score is: <###\n\t     Human:{user_score}    AI:{comp_score}\n")
            elif user_choice == 'scissors' and comp_choice == 'rock':
                print(f"\nYou have selected {user_choice.title()}")
                print(f"Computer choice is {comp_choice.title()}")
                print("Rock beats scissors CPU WINS\n")
                comp_score += 1
                print(f"\t###> The Score is: <###\n\t     Human:{user_score}    AI:{comp_score}\n")
            elif user_choice == 'rock' and comp_choice == 'paper':
                print(f"\nYou have selected {user_choice.title()}")
                print(f"Computer choice is {comp_choice.title()}")
                print("Paper beats rock CPU WINS!\n")
                comp_score += 1
                print(f"\t###> The Score is: <###\n\t     Human:{user_score}    AI:{comp_score}\n")
            elif user_choice == 'paper' and comp_choice == 'rock':
                print(f"\nYou have selected {user_choice.title()}")
                print(f"Computer choice is {comp_choice.title()}")
                print("Paper beats rock You WIN!\n")
                user_score += 1
                print(f"\t###> The Score is: <###\n\t     Human:{user_score}    AI:{comp_score}\n")
            elif user_choice == 'paper' and comp_choice == 'scissors':
                print(f"\nYou have selected {user_choice.title()}")
                print(f"Computer choice is {comp_choice.title()}")
                print("Scissors beats paper CPU WINS!\n")
                comp_score += 1
                print(f"\t###> The Score is: <###\n\t     Human:{user_score}    AI:{comp_score}\n")
            elif user_choice == 'scissors' and comp_choice == 'paper':
                print(f"\nYou have selected {user_choice.title()}")
                print(f"Computer choice is {comp_choice.title()}")
                print("Scissors beats paper You WIN!\n")
                user_score += 1
                print(f"\t###> The Score is: <###\n\t     Human:{user_score}    AI:{comp_score}\n")
            else:
                print("Ops wrong entry. Try again.")


intro()
main()
