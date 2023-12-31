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

        Args:
            width (int) : the width
            height (int) : the height
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
        Calculating the area for the rectangle
            method that has been BaseGeometry
        Calculating the area for the rectangle
            method that has been BaseGeometry

        Return : the area as integer.

        """
        return self.__width * self.__height

    def __str__(self):
        """
        A string methode that return a frinedla msg
        A string methode that return a frinedla msg
        A string methode that return a frinedla msg

        """
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
