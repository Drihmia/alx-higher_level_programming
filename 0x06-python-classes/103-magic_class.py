#!/usr/bin/python3

"""class magic for byte code"""


class MagicClass:
    radius = 0

    def __init__(self):
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
