#!/usr/bin/python3

def add_attribute(obj, name, value):
    if '__slots__' in dir(obj) or "__dict__" not in dir(obj):
        raise TypeError("can't add new attribute")
    obj.name = value
    return obj.name
