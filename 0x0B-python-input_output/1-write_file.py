#!/usr/bin/python3
""" opening a file and write on it """


def write_file(filename="", text=""):
    """ open a file in write mode and write a string into it"""

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
