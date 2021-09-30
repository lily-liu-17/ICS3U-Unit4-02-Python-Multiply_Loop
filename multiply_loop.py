#!/usr/bin/env python3

# Created by: Lily Liu
# Created on: Sept 2021
# This program takes the number you entered and multiplies
# all the previous numbers including the number entered


def main():
    # This program takes the number you entered and multiplies
    # all the previous numbers including the number entered
    # variables are set to 1 or else answer will be zero
    loop_counter = 1
    product = 1

    # Input
    user_input = input("Please a positive interger : ")

    try:
        # Process and Output
        user_input = int(user_input)
        if user_input < 0:
            print("You did not enter a positive integer")
        else:
            while loop_counter <= user_input:
                product = product * loop_counter
                loop_counter += 1
            print("{0}! is {1}".format(user_input, product))
    except Exception:
        print("Invalid input")

    print("")
    print("Done.")


if __name__ == "__main__":
    main()
