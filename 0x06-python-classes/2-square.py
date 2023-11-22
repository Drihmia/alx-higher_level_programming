#!/usr/bin/python3

"""Documentation for Square class """


class Square:
    """Empty class Square that defines a square."""

    def __init__(self, size):
        """Initialize the Square instance.

        Raises:
            ValueError: If the given size is negative.
            TypeError: If the given size is not an integer.
        """

        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
