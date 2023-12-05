#!/usr/bin/python3
"""
this module contain funtion that add new attribute to a object if its possible
"""


def add_attribute(obj, name, value):
    """Return  the name of attribute that has been added by this function
    Raise:
        TypeError : can't add new attribute is it is not possible
    """

    if '__slots__' in dir(obj) or "__dict__" not in dir(obj):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
