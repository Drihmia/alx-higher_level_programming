#!/usr/bin/python3
""" opening a file """


def read_file(filename=""):
    """ open a file in read only mode and read it"""

    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
