#!/usr/bin/python3
""" Module that contains a function called load_from_json_file. """
import json


def load_from_json_file(filename):
    """ A function that creates an Object from a “JSON file”
    """
    with open(filename, "r", encoding="utf-8") as f:
        # fl = f.read()
        return json.load(f)
