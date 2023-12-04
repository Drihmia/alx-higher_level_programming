#!/usr/bin/python3
"""
Thise module contain a funtion that  that returns the list of available
    attributes and methods of an object.
"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object"""

    return type(obj).__dir__(obj)
