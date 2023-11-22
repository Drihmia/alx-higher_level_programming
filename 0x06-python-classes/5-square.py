#!/usr/bin/python3

"""Documentation for Square class """


class Square:
    """Empty class Square that defines a square."""

    def __init__(self, size=0):
        """Initialize the Square instance.

        Args:
            size (int): The size of the square. Must be a non-negative integer.

        Raises:
            ValueError: If the given size is negative.
            TypeError: If the given size is not an integer.
        """

        self.size = size

    @property
    def size(self):
        """Get or set the size of the square.

        Returns:
            int: The current size of the square.
        """

        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size for the square.
                Must be a non-negative integer.

        Raises:
            ValueError: If the given size is negative.
            TypeError: If the given size is not an integer.

        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Compute the area of a given square.

        Returns:
            int : The return value. current square area.
        """
        return self.__size * self.__size

    def my_print(self):
        """Prints in stdout the square with the character #.

        If size is equal to 0, print an empty line.

        """
        for i in range(self.size):
            if i != 0:
                print()
            for j in range(self.size):
                print("#", end="")
        print()
