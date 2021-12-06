# Program 1: Lottery
# Create a program that ask 3 numbers (0-9) from the user.
# Generate 3 random winning numbers (0-9)
# Display “Winner” if all 3 input numbers matched the generated numbers
# Display ”You loss” if not
# Display ”Try again y/n” after each game
# If the user enter “y” the user will play again
# if “n” the program will exit.

import random

# computer will generate 3 random numbers between 0 to 9.


def get_num_comp():
    num_comp = []
    for i in range(0, 3):
        num_comp.append(random.randint(0, 9))
    return num_comp

# User will input 3 random number between 0 to 9.


def get_user_num():
    user_num = []
    for i in range(0, 3):
        user_guess = int(input("Put your lucky number: "))
    user_num.append(user_guess)
    return user_guess


int_comp = get_num_comp()
int_user = get_user_num()

# In this part we will know if the user inputed numbers are correct


def next_millionere():
    # If correct the output will be winner.
    if int_comp == int_user:
        print('--------------------------------------------')
        print("Winner")
        print("You are the new millionire!")
    else:
        # If wrong the out will be you loss.
        print('--------------------------------------------')
        print(f"You Loss.")
        print(
            f"The lucky combination are {int_comp[0]}, {int_comp[1]}, {int_comp[2]}")


next_millionaire()


# In this part we will ask the user if He or She wants to play again.
def kill_game():
    # asks the user if they want to play again
    print('--------------------------------------------')
    retry = input('Do you want to play again? (y/n) ')
    print('--------------------------------------------')
    # If yes user will once again be ask 3 random numbers
    if retry[0] == 'y':
        get_num_comp()
        get_user_num()
        next_millionere()
        print('--------------------------------------------')
    # If no the programm will end.
    elif retry[0] == 'n':
        exit


kill_game()
