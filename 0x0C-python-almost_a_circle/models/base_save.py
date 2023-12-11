#!/usr/bin/python3
"""
This module contains a class called Base
"""


class Base:
    """
    This class will be the “base” of all other classes in this project.

    Attributes:
        nb_objects : private class attribute.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
        print(self.__dict__)
        print()
        print()
        for ele in type(self).__dict__:
            print(f"{ele} : {type(self).__dict__[ele]}")
        print()
