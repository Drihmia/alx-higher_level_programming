#!/usr/bin/python3
"""
Modulle that contain a function called class_to_json that takes
a Python object
"""


def class_to_json(obj):
    """
     a function that returns the dictionary description with simple data
    structure (list, dictionary, string, integer and boolean) for JSON
    serialization of an object:
    """
    if obj:
        return obj.__dict__
