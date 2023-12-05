#!/usr/bin/python3
"""
this file contain a function calls append_after
"""


def append_after(filename="", search_string="", new_string=""):
    """
    This function inserts a line of text to a file, after each
        line containing a specific string.
    Args:
        search_string (str): target string.
        new_string (str): replacement string.
    """

    with open(filename, "r", encoding="utf-8") as f:
        list_lines = f.readlines()
        lines_write = []
        for line in list_lines:
            lines_write.append(line)
            if search_string in line:
                lines_write.append(new_string)

    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(lines_write)
