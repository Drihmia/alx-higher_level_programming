#!/usr/bin/python3
"""
this module contains one funtion that prints
    My name is <first name> <last name>.

>>> say_my_name("John", "Smith")
My name is John Smith

"""


def say_my_name(first_name, last_name=""):
    """Return None, print a string to stdout:
        My name is <first name> <last name>

    >>> say_my_name("John", "Smith")
    My name is John Smith
    >>> say_my_name("Walter", "White")
    My name is Walter White
    >>> say_my_name("Bob")
    My name is Bob
    >>> say_my_name(12, "White")
    Traceback (most recent call last):
    TypeError: first_name must be a string
    >>> say_my_name([1, 2], "White")
    Traceback (most recent call last):
    TypeError: first_name must be a string
    >>> say_my_name(None, "White")
    Traceback (most recent call last):
    TypeError: first_name must be a string
    >>> say_my_name("Redouane", 9)
    Traceback (most recent call last):
    TypeError: last_name must be a string
    >>> say_my_name("Redouane", (5, 8))
    Traceback (most recent call last):
    TypeError: last_name must be a string
    >>> say_my_name("Redouane", None)
    Traceback (most recent call last):
    TypeError: last_name must be a string
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is", first_name, last_name)


if __name__ == "__main__":
    import doctest
    flags = doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS | doctest.FAIL_FAST
    doctest.testmod(optionflags=flags)
