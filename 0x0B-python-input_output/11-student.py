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

    def to_json(self, lst=[]):
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
                return self.__dict__
            dic = {}
            for ele in lst:
                try:
                    getattr(self, ele)
                except Exception as e:
                    continue
                atr = getattr(self, ele)
                dic[ele] = atr
            return dic

    def reload_from_json(self, json):
        """ A method that replaces all attributes of the Student instance.

            Args : (dict) json is always a dictionary
        """
        if json is not None and len(json):
            setattr(self, "first_name", json["first_name"])
            setattr(self, "last_name", json["last_name"])
            setattr(self, "age", json["age"])
