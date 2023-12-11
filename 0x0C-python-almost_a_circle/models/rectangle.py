#!/usr/bin/python3
"""
this module contains a class called Rectangle that inherits from
    a class called Base.
"""
from models.base import Base


class Rectangle(Base):
    """This class inherits from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # getter and setter for width ------------------------------------
    @property
    def width(self):
        """ Getter for width private instance attribute. """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set the value of the width private instance attribute.
        Raises:
            TypeError: width must be an integer, if not raise error.
            ValueError: width must be > 0, if not raise error.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    # getter and setter for height ------------------------------------
    @property
    def height(self):
        """ Getter for height private instance attribute. """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set the value of the height private instance attribute.
        Raises:
            TypeError: height must be an integer, if not raise error.
            ValueError: height must be > 0, if not raise error.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    # getter and setter for x ------------------------------------
    @property
    def x(self):
        """ Getter for x private instance attribute. """
        return self.__x

    @x.setter
    def x(self, value):
        """ Set the value of the x private instance attribute.
        Raises:
            TypeError: x must be an integer, if not raise error.
            ValueError: x must be >= 0, if not raise error.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    # getter and setter for y ------------------------------------
    @property
    def y(self):
        """ Getter for y private instance attribute. """
        return self.__y

    @y.setter
    def y(self, value):
        """ Set the value of the y private instance attribute.
        Raises:
            TypeError: y must be an integer, if not raise error.
            ValueError: y must be >= 0, if not raise error.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Compute the are of the rectangle objects """
        return self.width * self.height

    def display(self):
        """ Display, prints in stdout the Rectangle instance
        with the character #
        """

        line = (" " * self.x + "#" * self.width + "\n")
        c = "\n" * self.y + line * self.height
        print(c[:-1])

    def __str__(self):
        """ return a string : [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        st = "[Rectangle] ({}) {}/{} - {}/{}"
        return st.format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ a funtion that update the Rectangle instance that assigns
            an argument to each attribute.
            for : id, widht, height, x and y.
        Note:
            **kwargs must be skipped if *args exists and is not empty
        """
        self.__a = 1
        lst = ["id", "width", "height", "x", "y"]
        for i in range(len(args)):
            setattr(self, lst[i], args[i])
            self.__a = 0
        if self.__a:
            for key, value in kwargs.items():
                if key in lst:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        A methode that returns the dictionary representation of
            a Rectangle's instances.
        """
        dict_d = {}
        list_d = ["id", "width", "height", "x", "y"]
        for ele in list_d:
            dict_d[ele] = getattr(self, ele)
        return dict_d
