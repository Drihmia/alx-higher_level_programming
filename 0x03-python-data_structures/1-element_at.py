#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < len(my_list) and idx >= 0:
        return [ele for (i, ele) in enumerate(my_list) if i == idx][0]
