#!/usr/bin/python3

class Square:
    """
    A class Square that defines a square.

    Args:
        size (int) : The first field.

    the size nust be an integer and greater or equal to 0.
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Compute the area of a given square.

        Returns:
            int : the current square area.
        """
        return self.__size * self.__size
