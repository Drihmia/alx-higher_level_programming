#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f"Last digit of {number} is ", end="")

if number < 0:
    number = number % 10 - 10
else:
    number %= 10
if number == 0:
    print(str(number) + " and is 0")
elif number > 5:
    print(str(number) + " and is greater than 5")
else:
    print(str(number) + " and is less than 6 and not 0")
