#!/usr/bin/python3
"""
This module contains one funtion that a class that inherits from list
"""


class MyList(list):
    """MyList (child class) inherits from list class (parent class)"""

    def print_sorted(self):
        my_list = self.copy()
        my_list.sort()
        print(my_list)
