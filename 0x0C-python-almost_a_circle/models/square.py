#!/usr/bin/python3
"""
This module contains a class called Square that ihnherits
    f**m the class called Rectangle.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class that represente a square object, which is a special
    case of a rectangle.

    Args:
        size (int) the side lenght of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Updating the str methode so it print information
            about the square instance.
        """
        st = "[Square] ({}) {}/{} - {}"
        return st.format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """
        Getter for the size property (equivalent to width for a square).

        Returns:
            int: The side length of the square.
        """
        return getattr(self, "width")

    @size.setter
    def size(self, value):
        """
        Setter for the size property.

        Args:
            value (int): The new side length value.
        """
        # super(Square, Square).width.fset(self, value)
        # super(Square, Square).height.fset(self, value)

        setattr(self, "width", value)
        setattr(self, "height", value)

    def update(self, *args, **kwargs):
        """ a funtion that update the square instance that assigns
            an argument to each attribute.
            for : id, size, x and y.
        Note:
            **kwargs must be skipped if *args exists and is not empty
        """
        self.__a = 1
        lst = ["id", "size", "x", "y"]
        for i in range(len(args)):
            setattr(self, lst[i], args[i])
            self.__a = 0

        if self.__a:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        A methode that returns the dictionary representation of
            a Square's instances.
        """
        dict_d = {}
        list_d = ["id", "size", "x", "y"]
        for ele in list_d:
            dict_d[ele] = getattr(self, ele)
        return dict_d
