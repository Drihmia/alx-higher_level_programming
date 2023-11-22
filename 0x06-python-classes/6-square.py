#!/usr/bin/python3

class Square:
    """
    A class Square that defines a square.


    the size nust be an integer and greater or equal to 0.
    """
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[0], int) or not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    # setting and getting the size field.

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

    # setting and getting the position field.

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Compute the area of a given square.

        Returns:
            int : the current square area.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints in stdout the square with the character #.

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

