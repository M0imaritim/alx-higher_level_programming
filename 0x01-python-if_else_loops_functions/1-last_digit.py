#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    last_digi = number % 10
if number < 0:
    last_digi = number % -10
if last_digi > 5:
    print(f"Last digit of {number} is {last_digi} and is greater than 5")
elif last_digi == 0:
    print(f"Last digit of {number} is {last_digi} and is 0")
elif last_digi and last_digi != 0:
    print(f"Last digit of {number} is {last_digi} and is less than 6 "
          f"and not 0")
