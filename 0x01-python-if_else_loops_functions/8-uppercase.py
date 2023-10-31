#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        if ch >= 'a' and ch <= 'z':
            ch = chr(ord(ch) - ord(" "))
        print("{}".format(ch), end="")
    print("")
