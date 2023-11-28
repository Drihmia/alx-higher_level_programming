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
    """Class Rectangle that define a rectangle

    Attributes:
        number_of_instances (int) : keep track of current number of instances
        print_symbol (str) : Used as symbol for string representation,
            can be any type, Initialized to #.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize the Rectangle instance.

        >>> my_rectangle = Rectangle(2, 4)
        >>> "{:d} instances of Rectangle".format(Rectangle.number_of_instances)
        '1 instances of Rectangle'
        >>> dictio = my_rectangle.__dict__
        >>> dictio["_Rectangle__height"] == 4
        True
        >>> dictio["_Rectangle__width"] == 2
        True
        >>> my_rectangle = Rectangle(5)
        Bye rectangle...
        >>> "{:d} instances of Rectangle".format(Rectangle.number_of_instances)
        '1 instances of Rectangle'
        >>> dictio = my_rectangle.__dict__
        >>> dictio["_Rectangle__height"] == 0
        True
        >>> dictio["_Rectangle__width"] == 5
        True
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Compute the area of the rectangle

        >>> my_rectangle = Rectangle(2, 4)
        >>> print("Area: {}".format(my_rectangle.area()))
        Area: 8
        >>> my_rectangle = Rectangle(0, 4)
        Bye rectangle...
        >>> print("Area: {}".format(my_rectangle.area()))
        Area: 0
        >>> my_rectangle = Rectangle(2, 0)
        Bye rectangle...
        >>> print("Area: {}".format(my_rectangle.area()))
        Area: 0
        >>> my_rectangle = Rectangle(2)
        Bye rectangle...
        >>> print("Area: {}".format(my_rectangle.area()))
        Area: 0
        >>> my_rectangle = Rectangle()
        Bye rectangle...
        >>> print("Area: {}".format(my_rectangle.area()))
        Area: 0
        """

        return self.__width * self.__height

    def perimeter(self):
        """Compute the perimeter of the rectangle

        Returns:
            int : positive value
        >>> my_rectangle = Rectangle(2, 4)
        >>> print("perimeter: {}".format(my_rectangle.perimeter()))
        perimeter: 12
        >>> my_rectangle = Rectangle(0, 4)
        Bye rectangle...
        >>> print("perimeter: {}".format(my_rectangle.perimeter()))
        perimeter: 0
        >>> my_rectangle = Rectangle(4, 0)
        Bye rectangle...
        >>> print("perimeter: {}".format(my_rectangle.perimeter()))
        perimeter: 0
        >>> my_rectangle = Rectangle(4)
        Bye rectangle...
        >>> print("perimeter: {}".format(my_rectangle.perimeter()))
        perimeter: 0
        >>> my_rectangle = Rectangle()
        Bye rectangle...
        >>> print("perimeter: {}".format(my_rectangle.perimeter()))
        perimeter: 0
        """

        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Implementing the __str__ magic method so that the object
            return a rectangle of squares.

        >>> my_rectangle = Rectangle(2, 4)
        >>> print(str(my_rectangle))
        ##
        ##
        ##
        ##
        >>> print(repr(my_rectangle))
        Rectangle(2, 4)
        >>> my_rectangle = Rectangle(0, 4)
        Bye rectangle...
        >>> print(str(my_rectangle))
        <BLANKLINE>
        >>> print(repr(my_rectangle))
        Rectangle(0, 4)
        >>> my_rectangle_1 = Rectangle(2, 4)
        >>> my_rectangle_1.print_symbol = "&"
        >>> my_rectangle_1.print_symbol
        '&'
        >>> print(str(my_rectangle_1))
        &&
        &&
        &&
        &&
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        square = (str(self.print_symbol) * self.__width + "\n") * self.__height
        return square[:-1]

    def __repr__(self):
        """Implementing the __repr__ magic method so that the object
            return a string representation of the rectangle to be able
            to recreate a new instance by using eval() (see example below).

        >>> my_rectangle = Rectangle(2, 4)
        >>> print(str(my_rectangle))
        ##
        ##
        ##
        ##
        >>> print(my_rectangle)
        ##
        ##
        ##
        ##
        >>> print(repr(my_rectangle))
        Rectangle(2, 4)
        >>> print(hex(id(my_rectangle)))
        ... # doctest +ELLIPSIS
        0x...
        >>> new_rectangle = eval(repr(my_rectangle))
        >>> print(str(new_rectangle))
        ##
        ##
        ##
        ##
        >>> print(str(new_rectangle))
        ##
        ##
        ##
        ##
        >>> print(repr(new_rectangle))
        Rectangle(2, 4)
        >>> print(hex(id(new_rectangle)))
        ... # doctest +ELLIPSIS
        0x...
        >>> print(new_rectangle is my_rectangle)
        False
        >>> print(type(new_rectangle) is type(my_rectangle))
        True
        """
        h = self.__height
        w = self.__width
        return "Rectangle(" + str(w) + ", " + str(h) + ")"

    def __del__(self):
        """Impliment the __del__ magic methode to print
            Bye rectangle... to stdout while deleting
            is captured
        >>> my_rectangle = Rectangle(2, 4)
        >>> l = "Area: {} - Perimeter: {}"
        >>> print(l.format(my_rectangle.area(), my_rectangle.perimeter()))
        Area: 8 - Perimeter: 12
        >>> del my_rectangle
        Bye rectangle...
        >>> print(my_rectangle)
        Traceback (most recent call last):
        NameError: name 'my_rectangle' is not defined
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area.

        Raises:
            TypeError: rect_1 must be an instance of Rectangle
            TypeError: rect_2 must be an instance of Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return (repr(rect_1))
        elif rect_1.area() < rect_2.area():
            return (repr(rect_2))
        else:
            return (repr(rect_1))

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with width == height == size"""

        return cls(size, size)


if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS | doctest.FAIL_FAST)
