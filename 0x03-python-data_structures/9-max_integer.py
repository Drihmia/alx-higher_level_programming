#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list != []:
        return sorted(my_list, reverse=True)[0]
