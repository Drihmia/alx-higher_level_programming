#!/usr/bin/python3
"""
A class with no class or object attribute, that prevents the user from
    dynamically creating new instance attributes, except
    if the new instance attribute is called first_name.
"""


class LockedClass:
    """Preventing the user from dinamically creating a
        new instance attribute"""

    __slots__ = ('first_name',)
