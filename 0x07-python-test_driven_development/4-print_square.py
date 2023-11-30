#!/usr/bin/python3
"""
This module contains one funtion that prints a square with the character #.

>>> print_square(4)
####
####
####
####
"""


def print_square(size):
    """Return None, prints a square with the character #.

    >>> print_square(2.2)
    ##
    ##
    >>> print_square(4)
    ####
    ####
    ####
    ####
    >>> print_square(0)
    >>> print_square(1)
    #
    >>> print_square(-1)
    Traceback (most recent call last):
    ValueError: size must be >= 0
    >>> print_square(-1.0)
    Traceback (most recent call last):
    TypeError: size must be an integer
    >>> print_square("22")
    Traceback (most recent call last):
    TypeError: size must be an integer
    >>> print_square([2, 3])
    Traceback (most recent call last):
    TypeError: size must be an integer
    """

    if type(size) not in [int, float]:
        raise TypeError("size must be an integer")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    print(("#" * int(size) + "\n") * int(size), end="")


if __name__ == "__main__":
    import doctest
    flags = doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS | doctest.FAIL_FAST
    flag = doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS
    doctest.testmod(optionflags=flag)
