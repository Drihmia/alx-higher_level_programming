#!/usr/bin/python3

class Square:
    """
    A class Square that defines a square.

    Args:
        size (int) : The first field.

    the size nust be an integer and greater or equal to 0.
    """
    def __init__(self, size=0):
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
