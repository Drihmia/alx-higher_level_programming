#!/usr/bin/python3
"""
file that contain a class called MyInt inherits F**m int
"""


class MyInt(int):
    """A rebel classe the invert the behivor of

        equal and not equal magic methods
        of int class
    """
    def __ne__(self, other):
        return not super().__ne__(other)

    def __eq__(self, other):
        return not super().__eq__(other)
