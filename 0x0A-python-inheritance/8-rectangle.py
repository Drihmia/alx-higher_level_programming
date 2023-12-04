#!/usr/bin/python3
"""
this module contain a classe called Rectangle that inherits
from Base Geometry class
"""


class Rectangle(__import__("7-base_geometry").BaseGeometry):
    """  a classe that inherits from BaseGeometry (7-base_geometry.py)"""

    def __init__(self, width, height):
        """
        Instantiation with width and height

        Raises:
            ValueError: from integer_validator;
                width and height must be positive integers
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
