#!/usr/bin/python3

"""class magic for byte code"""


class MagicClass:

    """Class magic class for byte code.

    Attributes:
        radius: integer or float : or radias of a circle.
    """

    def __init__(self):
        """Initialize the MagicClass instance.

        Raises:
            TypeError: if the given radius is not a float or and int.

        """

        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self._MagicClass__radius = radius

    def area(self):
        """Compute the area of a given circl.

        Returns:
            float : the current circl area.
        """
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """Compute the circumference of a given circl.

        Returns:
            float : the current circl circumference.
        """
        return 2 * math.pi * self._MagicClass__radius
