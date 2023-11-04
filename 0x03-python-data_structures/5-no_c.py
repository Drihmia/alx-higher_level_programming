#!/usr/bin/python3
def no_c(my_string):
    for (i, ch) in enumerate(my_string):
        if ch in "cC":
            my_string = my_string[:i] + my_string[i + 1:]
    return my_string
