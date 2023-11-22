#!/usr/bin/python3

"""class magic for byte code"""


class MagicClass:

    """Class magic class for byte code."""

    def __init__(self, radius=0):
        """Initialize the MagicClass instance.

        Args:
            radius: integer or float : or radias of a circle.

        Raises:
            TypeError: if the given radius is not a float or and int.

        """

        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Compute the area of a given circl.

        Returns:
            float : the current circl area.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Compute the circumference of a given circl.

        Returns:
            float : the current circl circumference.
        """
        return 2 * math.pi * self.__radius
