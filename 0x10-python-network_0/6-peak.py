#!/usr/bin/python3
"""
# Technical interview preparation:
# - I am not allowed to google anything
# - Whiteboard first
# Problem: 
# Write a function that finds a peak in a list of unsorted integers.
# - Prototype: def find_peak(list_of_integers):
# - I am not allowed to import any module
# - My algorithm must have the lowest complexity
#   - (hint: I don’t need to go through all numbers to find a peak)
"""


def find_peak(list_of_integers):
    """a function that finds a peak in a list of unsorted integers."""

    if list_of_integers:
        for i in range(1, len(list_of_integers)):
            if (list_of_integers[i] >= list_of_integers[i - 1] and
                list_of_integers[i] >= list_of_integers[i + 1]):
                return  list_of_integers[i]
