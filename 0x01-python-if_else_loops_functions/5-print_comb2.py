#!/usr/bin/python3
for digit in range(100):
    print("{0:02d}".format(digit), end=", " if digit < 99 else "\n")
