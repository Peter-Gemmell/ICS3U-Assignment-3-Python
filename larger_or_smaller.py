#!/usr/bin/env python3

# Created by Peter Gemmell
# Created on April 2022
# This program indicates between 2 numbers which is larger or smaller


def main():
    # This function indicates between 2 numbers which is larger or smaller

    # input
    print(
        "This program tells the user if a number is larger or smaller than the other."
    )
    number_1_string = input("Enter the first number: ")
    number_2_string = input("Enter the second number: ")
    print("")

    # process & output
    try:
        number_1 = int(number_1_string)
        number_2 = int(number_2_string)
        if number_1 > number_2:
            print("The first number {} is larger than the second number {}.".format(number_1, number_2))
        elif number_1 < number_2:
            print("The second number {} is larger than the first number {}.".format(number_2, number_1))
        else:
            print("the first number {} is equal to the second number {}.".format(number_1, number_2))

    except Exception:
        print("Invalid numbers entered, please try again.")
    print("Done.")


if __name__ == "__main__":
    main()
