
# Generate 1 random number (0-100)
# Ask the user to guess the number
# Display “Greater than” if the inputed number is greater than the random number
# Display “Less than” if the inputed number is less than the random number
# Repeat asking the user until the random number has been guessed correctly.

import random

comp_num = random.randrange(0, 100)
user_guess = False


while user_guess == False:
    # user will input a random number between 0 - 100
    insert_num = int(input("Please input a number between 0 and 100:"))
    user_num = int(insert_num)
    # evaluate if user_num is less than comp_num
    if user_num < comp_num:
        # Give hit about the comp_guess
        print("Greater than")
    # evaluate if user_num is greater than comp_num
    elif user_num > comp_num:
        # give hit about the comp_guess
        print("Less than")
    else:
        # user_num is the same with comp_num
        if user_num == comp_num:
            # user get the correct answer
            print("Are you a sage? Because you guess it right.")
