#!/usr/bin/python3

"""Documentation for Square class """


class Square:
    """Empty class Square that defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the Square instance.

        Args:
            size (int): The size of the square. Must be a non-negative integer.
            position (tuple):  must be a tuple of 2 positive integers.

        Raises:
            ValueError: If the given size is negative.
            TypeError: If the given size is not an integer or
                position is not a tuple of 2 positive integers.
        """
        self.size = size
        self.position = position

    # setting and getting the size field.

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

    # setting and getting the position field.

    @property
    def position(self):
        """Get or set the position of the square.

        Returns:
            tuple: The current position of the square.
        """

        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): The new position for the square.
                Must be a tuple of 2 positive integers.

        Raises:
            TypeError: If the given position is not a tuple
                of 2 positive integers.

        """

        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Compute the area of a given square.

        Returns:
            int : the current square area.
        """
        return self.__size * self.__size

    def my_print(self):
        """Prints in stdout the square with the character #.

        If size is equal to 0, print an empty line.
        """
        if self.size == 0:
            print()
            return
        for i in range(self.__size + self.position[1]):
            if i < self.position[1]:
                print()
            else:
                if i != self.position[1]:
                    print()
                for j in range(self.size + self.position[0]):
                    print(" " if j < self.position[0] else "#", end="")
        print()

    def __str__(self):
        """Returning a string

        If size is equal to 0, print an empty line.
        """

        strr = ""
        if self.size == 0:
            strr = ""
            return strr
        for i in range(self.position[1]):
            strr = "\n" * self.position[1]
        for j in range(self.size):
            strr = strr + " " * self.position[0] + "#" * self.size + "\n"
        return strr[:-1]
