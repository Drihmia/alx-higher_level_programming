#!/usr/bin/python3
"""
this a script that reads fron stdin line by line and computes metrics.
this a script that reads fron stdin line by line and computes metrics.
"""
import sys


def main():
    """
    main funtion : entry point
    """

    dic = {}
    total_size = 0
    while True:
        N_lines = 0
        for lin in sys.stdin:
            N_lines += 1
            line = lin.split()
            total_size += int(line[-1])
            tmp = line[-2]
            if tmp in dic:
                dic[tmp] += 1
            else:
                dic[tmp] = 1
            if N_lines >= 10:
                break
        dic = dict(sorted(dic.items()))
        for key, value in dic.items():
            print(str(key) + ":", value)
        print("File size:", total_size)


if __name__ == "__main__":
    main()
