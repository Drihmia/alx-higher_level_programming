#!/usr/bin/python3
BaseGeometry = __import__("7-base_geometry").BaseGeometry
"""
this module contain a classe called Rectangle that inherits
f**m Base Geometry class
"""


class Rectangle(BaseGeometry):
    """A classe that inherits f**m BaseGeometry (7-base_geometry.py)

    """

    def __init__(self, width, height):
        """
        Instantiation with width and height

        Raises:
            ValueError:  integer_validator;
                width and height must be positive integers
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        calculating the area for the rectangle
            method that has been BaseGeometry
        """
        return self.__width * self.__height

    def __str__(self):
        """a string methode that return a frinedla msg

        """
        ha = self.__class__.__name__
        return "[{}] {}/{}".format(ha, self.__width, self.__height)
