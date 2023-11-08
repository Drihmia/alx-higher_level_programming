#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        m = max(a_dictionary.values())
        for item in a_dictionary.items():
            if item[1] == m:
                return item[0]
