#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = 10 - number % 10
    else:
        number %= 10
    print("{0:d}".format(number), end="")
    return number
