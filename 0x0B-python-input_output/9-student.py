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

    def to_json(self):
        """
        A method that retrieves a dictionary representation of a
        Student instance (same as 8-class_to_json.py).
        """
        return self.__dict__
