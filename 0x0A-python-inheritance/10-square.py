#!/usr/bin/python3
"""
this module contain a classe called Square that inherits
f**m Base Rectangle class
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """A classe that inherits f**m BaseGeometry (7-base_geometry.py)

    """

    def __init__(self, size):
        """
        Instantiation with size

        Args:
            size : integer
        Raises:
            ValueError:  integer_validator;
                size must be positive integers
        """

        self.integer_validator("size", size)
        self.__size = size
        self.__width = size
        self.__height = size

    def area(self):
        """
        Calculating the area for the rectangle
            method that has been BaseGeometry
        Calculating the area for the rectangle
            method that has been BaseGeometry

        Return : the area as integer.

        """
        return self.__size ** 2

    def __str__(self):
        """
        A string methode that return a frinedla msg
        A string methode that return a frinedla msg
        A string methode that return a frinedla msg

        """
        return "[Rectange] " + str(self.__width) + "/" + str(self.__height)
