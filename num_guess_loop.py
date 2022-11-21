#!/usr/bin/env python3
#
# Created by: Nolan Shami
# Created on: Nov 21, 2022
# This program generates a random correct guess.
# It then uses a loop to keep asking the user to guess
# the number until they guess correctly.
# Once they guess the correct number, it breaks out of the loop.

import random


def main():
    # declare the loop counter
    loop_counter = 0
    # generating a random number from 0 to 9
    random_number = random.randint(0, 9)

    # using a loop to keep asking for a number until they guessed it right
    while True:
        # set the user number as a string
        user_num_string = input("Enter a whole number between 0 and 9: ")
        try:
            # convert it from string into integer
            user_num = int(user_num_string)
            # Check to see if they actually did input a number from 0 to 9
            if user_num >= 0 and user_num <= 9:
                # Increment the counter by 1
                loop_counter += 1
                # check if they guessed correctly
                if user_num == random_number:
                    # Display if they guessed it right
                    print(" ")
                    print("{} is correct, good job!".format(user_num))
                    # break out of the loop
                    break
                else:
                    # if they are wrong, keep going
                    # Display result to user
                    print("{} is incorrect".format(user_num))
                    print(" ")
                    print("Tracking {0} times through the loop.".format(loop_counter))
                    print(" ")
            else:
                # display if the given number isn't from 0 to 9
                print("This whole number is not between 0 and 9")
                print(" ")
        # exception for erroneous input from the user
        except Exception:
            print(" I feel like {} is either a decimal or a text...please enter a whole number between 0 and 9!".format(user_num_string))
            print(" ")


if __name__ == "__main__":
    main()
