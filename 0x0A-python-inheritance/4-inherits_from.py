#!/usr/bin/python3
"""
in this module, we find a function that checks if an object is an instance,
or if the object is an instance of a class that inherited (directly
or indirectly) from, the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """Returns True if an object is an instance,
    or if the object is an instance of a class that inherited (directly
    or indirectly) from, the specified class ; otherwise False."""

    if isinstance(obj, a_class) and obj.__class__ != a_class:
        return True
    return False
