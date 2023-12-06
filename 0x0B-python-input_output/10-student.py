#!/usr/bin/python3
"""
This module contain a class called Student
"""


class Student:
    """ A class Student that defines a student by:
    Args:
        first_name (str) : name of student.
        last_name (str) : last name of student.
        age (int) : age of student.
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, lst=[-1]):
        """
        A method that retrieves a dictionary representation of a
        Student instance (same as 8-class_to_json.py).

        Args:
            lst (list) : a list if attributes

        - If attrs is a list of strings, only attribute names contained in
        this list must be retrieved.
        - Otherwise, all attributes must be retrieved

        """
        if type(lst) is list:
            if not len(lst):
                return {}
            if lst[0] == -1:
                return self.__dict__
            dic = {}
            dic_orig = self.__dict__
            for key, ele in dic_orig.items():
                if key in lst:
                    dic[key] = ele
            return dic
