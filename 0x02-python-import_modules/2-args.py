#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1
    if argc == 0:
        print("{0:d} arguments.".format(argc))
    elif argc == 1:
        print("{0:d} argument.".format(argc))
    else:
        print("{0:d} arguments:".format(argc))

    for i in range(1, argc + 1):
        print("{0:d}: {1:s}".format(i, sys.argv[i]))
