#!/usr/bin/python3
"""
in this module, we find a function that checks is an object is an instance
    of a specified class.
"""


def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance of the specified
    class, otherwise False."""

    if obj.__class__ == a_class:
        return True
    return False
