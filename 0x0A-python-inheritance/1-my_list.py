#!/usr/bin/python3
"""
This module contains one funtion that a class that inherits from list

"""


class MyList(list):
    """MyList (child class) inherits from list class (parent class)
    >>> MyList = __import__('1-my_list').MyList
    >>> my_list = MyList()
    >>> my_list.print_sorted()
    []
    >>> my_list.append(1)
    >>> my_list.print_sorted()
    [1]
    >>> my_list.print_sorted(None)
    Traceback (most recent call last):
    TypeError: MyList.print_sorted() takes 1 positional \
argument but 2 were given
    >>> my_list.append(4)
    >>> my_list.append(2)
    >>> my_list.append(3)
    >>> my_list.append(5)
    >>> print(my_list)
    [1, 4, 2, 3, 5]
    >>> my_list.print_sorted()
    [1, 2, 3, 4, 5]
    >>> print(my_list)
    [1, 4, 2, 3, 5]
    """

    def print_sorted(self):
        my_list = self.copy()
        my_list.sort()
        print(my_list)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
