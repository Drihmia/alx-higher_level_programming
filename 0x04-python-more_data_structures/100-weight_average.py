#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        S = [i[1] for i in my_list]
        SP = list(map(lambda i: i[0] * i[1], my_list))
        sum_s = sum(S)
        if not sum_s:
            return 0
        sum_sp = sum(SP)
        return sum_sp / sum_s
    return 0
