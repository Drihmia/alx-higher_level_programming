#!/usr/bin/python3
""" this module contain a function called from_json_string  """
import json


def from_json_string(my_obj):
    """ a function that returns an object (Python data structure)
    represented by a JSON string.

    """
    return json.loads(my_obj)
