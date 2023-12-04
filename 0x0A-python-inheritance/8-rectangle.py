#!/usr/bin/python3
"""
this module contain a classe called Rectangle that inherits
f**m Base Geometry class
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """A classe that inherits f**m BaseGeometry (7-base_geometry.py)

    """

    def __init__(self, width, height):
        """
        Instantiation with width and height

        Raises:
            ValueError: f**m integer_validator;
                width and height must be positive integers
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
