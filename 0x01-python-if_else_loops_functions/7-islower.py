#!/usr/bin/python3
import sys


def islower(c):
    if not c:
        print("Traceback (most recent call last): you have type anything")
        sys.exit()
    elif (c >= 'a' and c <= 'z'):
        return True
    return False
