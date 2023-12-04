#!/usr/bin/python3
"""
in this module, you shall find a Class called BaseGeometry
>>> bg = BaseGeometry()
>>> bg.integer_validator("my_int", 12)
>>> bg.integer_validator("width", 89)
>>> try:
...	    bg.integer_validator("name", "John")
... except Exception as e:
... 	print("[{}] {}".format(e.__class__.__name__, e))
[TypeError] name must be an integer

"""


class BaseGeometry:
    """A class with one public instance method called area and that raise
    an exception if that method is called

    Raises:
        -TypeError : value must be an integer
        -ValueError : value must be greater than 0

    >>> bg = BaseGeometry()
    >>> bg.integer_validator("my_int", 12)
    >>> bg.integer_validator("width", 89)
    >>> try:
    ...	    bg.integer_validator("name", "John")
    ... except Exception as e:
    ... 	print("[{}] {}".format(e.__class__.__name__, e))
    [TypeError] name must be an integer
    >>> try:
    ...     bg.integer_validator("age", 0)
    ... except Exception as e:
    ...     print("[{}] {}".format(e.__class__.__name__, e))
    [ValueError] age must be greater than 0
    >>> try:
    ...     bg.integer_validator("distance", -4)
    ... except Exception as e:
    ...     print("[{}] {}".format(e.__class__.__name__, e))
    [ValueError] distance must be greater than 0
    >>> try:
    ...     bg.integer_validator("distance", -4.43)
    ... except Exception as e:
    ...     print("[{}] {}".format(e.__class__.__name__, e))
    [TypeError] distance must be an integer
    >>> try:
    ...	    bg.integer_validator("name", ["John"])
    ... except Exception as e:
    ... 	print("[{}] {}".format(e.__class__.__name__, e))
    [TypeError] name must be an integer
    >>> try:
    ...	    bg.integer_validator("name", None)
    ... except Exception as e:
    ... 	print("[{}] {}".format(e.__class__.__name__, e))
    [TypeError] name must be an integer
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
