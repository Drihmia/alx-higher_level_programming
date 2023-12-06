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
    N_lines = 0
    try:
        for lin in sys.stdin:
            try:
                line = lin.split()
                total_size += int(line[-1])
                tmp = line[-2]
                tmp = int(tmp)
                if tmp in dic:
                    dic[tmp] += 1
                    N_lines += 1
                else:
                    N_lines += 1
                    dic[tmp] = 1
            except (IndexError, ValueError):
                continue
            if N_lines % 10 == 0:
                try:
                    dic = dict(sorted(dic.items()))
                except (IndexError, ValueError):
                    pass
                print("File size:", total_size, flush=True)
                for key, value in dic.items():
                    print(str(key) + ":", value, flush=True)
        print("File size:", total_size, flush=True)
        for key, value in dic.items():
            print(str(key) + ":", value, flush=True)
    except KeyboardInterrupt as e:
        sys.stdout.flush()
        print("File size:", total_size, flush=True)
        for key, value in dic.items():
            print(str(key) + ":", value, flush=True)


if __name__ == "__main__":
    main()
