#!/usr/bin/python3
"""
in this module, you shall find a Class called BaseGeometry
"""


class BaseGeometry:
    """A class with one public instance method called area and that raise
    an exception if that method is called"""
    def area(self):
        raise Exception("area() is not implemented")
