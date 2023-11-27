#!/usr/bin/python3

"""
this module contains one funtion that handle different aspect of a rectangle
    such as the area and the perimeter...

>>> rec = Rectangle()
>>> type(rec)
... # doctest +ELLIPSIS
<class '...Rectangle'>
"""


class Rectangle:
    """Class Rectangle that define a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize the Rectangle instance.

        >>> my_rectangle = Rectangle(2, 4)
        >>> dictio = my_rectangle.__dict__
        >>> dictio["_Rectangle__height"] == 4
        True
        >>> dictio["_Rectangle__width"] == 2
        True
        >>> my_rectangle = Rectangle(5)
        >>> dictio = my_rectangle.__dict__
        >>> dictio["_Rectangle__height"] == 0
        True
        >>> dictio["_Rectangle__width"] == 5
        True
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the value of width

        Returns:
            int : the width's value
        """

        return self.__width

    @width.setter
    def width(self, value):
        """Set the value of width
        Raises:
            TypeError: width must be an integer.
            ValueError: width must be >= 0.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the value of height

        Returns:
            int : the height's value
        """

        return self.__height

    @height.setter
    def height(self, value):
        """Set the value of height
        Raises:
            TypeError: height must be an integer.
            ValueError: height must be >= 0.
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value


if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)
