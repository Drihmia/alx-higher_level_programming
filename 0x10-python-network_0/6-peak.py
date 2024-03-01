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
        low = 0
        high = len(list_of_integers) - 1

        while low < high:
            mid = (low + high) // 2

            if list_of_integers[mid] > list_of_integers[mid + 1]:
                high = mid
            else:
                low = mid + 1

        return list_of_integers[low]
