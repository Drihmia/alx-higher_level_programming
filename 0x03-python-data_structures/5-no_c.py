#!/usr/bin/python3
def no_c(my_string):
    str1 = ""
    for ch in my_string:
        if ch not in "cC":
            str1 = str1 + ch
    return str1
