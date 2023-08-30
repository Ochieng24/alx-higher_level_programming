#!/usr/bin/python3
<<<<<<< HEAD
# 9-print_last_digit.py


def print_last_digit(number):
    """Print the last digit of a number and return it."""
    print(abs(number) % 10, end="")
    return (abs(number) % 10)

=======
def print_last_digit(number):
    if number > 0:
        last_digit = number % 10
    else:
        last_digit = (number % -10) * -1
    print("{}".format(last_digit), end="")
    return last_digit
>>>>>>> cdec887f77613d69d8107433ebf5f7871f48c5dc
