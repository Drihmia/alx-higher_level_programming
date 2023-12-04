#!/usr/bin/python3
"""
in this module, you shall find a Class called BaseGeometry
"""


class BaseGeometry:
    """A class with one public instance method called area and that raise
    an exception if that method is called"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
