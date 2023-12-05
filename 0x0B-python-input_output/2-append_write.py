#!/usr/bin/python3
""" opening a file and write on it """


def append_write(filename="", text=""):
    """ open a file in write mode and append a string into it"""

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
