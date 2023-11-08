#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary:
        a = a_dictionary
        [print("{}: {}".format(key, a[key])) for key in sorted(a.keys())]
