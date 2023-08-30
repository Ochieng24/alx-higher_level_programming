#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
<<<<<<< HEAD
digit = abs(number) % 10
if number < 0:
    digit = -digit
print("Last digit of {} is {} and is ".format(number, digit), end="")
if digit > 5:
    print("greater than 5")
elif digit == 0:
    print("0")
else:
    print("less than 6 and not 0")

=======
if number > 0:
    last_digit = number % 10
else:
    last_digit = number % -10

if last_digit > 5:
    print(f"Last digit of {number:d} is {last_digit:d} and is greater than 5")
elif last_digit < 6 and last_digit != 0:
    print(f"Last digit of {number:d} is {last_digit:d} and \
is less than 6 and not 0")
else:
    print(f"Last digit of {number:d} is {last_digit:d} and is 0")
>>>>>>> cdec887f77613d69d8107433ebf5f7871f48c5dc
