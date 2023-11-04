#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    len_l = len(my_list)
    new_list = []
    if idx >= 0 and idx < len_l:
        my_list[idx] = [element for i in range(len_l) if i == idx][0]
    return my_list
