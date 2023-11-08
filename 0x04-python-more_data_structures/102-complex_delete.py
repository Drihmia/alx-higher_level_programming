#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary and value:
        d = a_dictionary
        while value in a_dictionary.values():
            for x, y in d.items():
                if y == value:
                    del a_dictionary[x]
                    break
    return a_dictionary
