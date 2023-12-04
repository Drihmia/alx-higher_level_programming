#!/usr/bin/python3
"""
in this module, we find a function that checks if an object is an instance,
or if the object is an instance of a class that inherited from,
the specified class ; otherwise False..
"""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance of, or if the object
    is an instance of a class that inherited from, the specified class;
    otherwise False."""

    if isinstance(obj, a_class):
        return True
    return False
