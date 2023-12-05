#!/usr/bin/python3
""" module that conatins a script that adds al arguments
to a Python list, and then save them to a file called "add_item.json".
"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
tmp = load_from_json_file("add_item.json")
save_to_json_file(tmp + sys.argv[1:], "add_item.json")
print(load_from_json_file("add_item.json"))
