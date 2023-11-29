#!/usr/bin/python3
"""
this module contains one funtion that adds two number

>>> add_integer(1, 2)
3
>>> add_integer(100, -2)
98
"""


def add_integer(a, b=98):
    """Return the sum of two integer or floats, return an exact integer.

    a and b going to be first casted to integers if they are float.

    >>> add_integer(1, 2)
    3
    >>> add_integer(100, -2)
    98
    >>> add_integer(4, "School")
    Traceback (most recent call last):
    TypeError: b must be an integer
    >>> add_integer("Red", 3)
    Traceback (most recent call last):
    TypeError: a must be an integer
    >>> add_integer(None)
    Traceback (most recent call last):
    TypeError: a must be an integer
    >>> add_integer([2, 3], 3)
    Traceback (most recent call last):
    TypeError: a must be an integer

    """
    if a != a:
        raise TypeError("a must be an integer")
    if b != b:
        raise TypeError("b must be an integer")
    if a is None or type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if b is None or type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    if a == float('inf') or a == -float('inf'):
        return 0
    if b == float('inf') or b == -float('inf'):
        return 0

    result = int(a) + int(b)
    if result == float('inf') or result == -float('inf'):
        return 98
    return result


if __name__ == "__main__":
    import doctest
    flags = doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS
    doctest.testmod(optionflags=flags)
