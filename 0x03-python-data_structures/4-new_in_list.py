#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    len_l = len(my_list)
    new_list = []
    if idx >= 0 and idx < len_l:
        new_list = [element if i == idx else my_list[i] for i in range(len_l)]
    else:
        new_list = my_list
    return new_list
