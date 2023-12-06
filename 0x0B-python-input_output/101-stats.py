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
            try:
                line = lin.split()
                total_size += int(line[-1])
                tmp = line[-2]
                if tmp in dic:
                    dic[tmp] += 1
                else:
                    dic[tmp] = 1
            except Exception:
                continue
            if N_lines >= 10:
                break
        try:
            dic = dict(sorted(dic.items()))
        except Exception:
            continue
        finally:
            print("File size:", total_size)
            for key, value in dic.items():
                print(str(key) + ":", value)


if __name__ == "__main__":
    main()
