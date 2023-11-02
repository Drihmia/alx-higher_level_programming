#!/usr/bin/python3
import sys
if __name__ != "3-infinite_add":
    argc = len(sys.argv) - 1
    sum = 0
    for i in range(1, argc + 1):
        sum = sum + int(sys.argv[i])
    print("{0:=-d}".format(sum))
