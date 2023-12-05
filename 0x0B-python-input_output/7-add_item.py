#!/usr/bin/python3
""" module that conatins a script that adds al arguments
to a Python list, and then save them to a file called "add_item.json".
"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file_name = "add_item.json"
args = sys.argv
a = 0
try:
    open(file_name)
except Exception as e:
    a = 1
finally:
    tmp = []
    if a != 1:
        tmp = load_from_json_file(file_name)


save_to_json_file(tmp + sys.argv[1:], file_name)
