#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as er:
        sys.stderr.write("Exception: " + str(er) + "\n")
        return None
