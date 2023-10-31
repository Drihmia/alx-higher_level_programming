#!/usr/bin/python3

def islower(c):
    if not c:
        print("Traceback (most recent call last): you have type anything")
        return False
    elif (c >= 'a' and c <= 'z'):
        return True
    return False
