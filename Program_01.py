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
def get_number():
    num_comp = []
    for i in range(0, 3):
        winning_number = random.randint(0, 9)
        while winning_number in num_comp:
            winning_number = random.randint(0, 9)
        num_comp.sort
        num_comp.append(winning_number)
    return num_comp


def get_user_number():
    user_num = []
    for i in range(0, 3):
        # User will input 3 random number between 0 to 9.
        user_guess = int(input("Put your lucky number: "))
        user_num.sort
        user_num.append(user_guess)
    return user_num


def get_winner(int_comp, int_user):
    if int_comp == int_user:
        print("--------------------------------------------")
        print("Winner")
    else:
        print("--------------------------------------------")
        print("You loss")


def play_again():
    # asks the user if they want to play again
    print("--------------------------------------------")
    ask_user = input("Do you want to play again? (y/n) ")
    print("--------------------------------------------")
    # If yes user will once again be ask 3 random numbers
    if ask_user == "y":
        get_number()
        get_user_number()
        get_winner(int_comp, int_user)
        play_again()
        print("--------------------------------------------")
    # If no the programm will end.
    elif ask_user == "n":
        exit


int_comp = get_number()
int_user = get_user_number()
get_winner(int_comp, int_user)
play_again()
