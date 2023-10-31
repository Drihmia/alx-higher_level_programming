#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if not i % 3:
            print("Fizz", end="")
        if not i % 5:
            print("Buzz", end="")
        if i % 5 and i % 3:
            print(i, end="")
        if i < 101:
            print("", end=" ")
