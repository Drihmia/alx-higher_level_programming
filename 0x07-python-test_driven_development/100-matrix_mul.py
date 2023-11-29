#!/usr/bin/python3
"""
this module contains one funtion that divides all elements of a matrix.

"""

def matrix_mul(m_a, m_b):

    # checking the matrix.
    list_length = 0
    b = -9
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")

    # looping through the outer list of m_a.
    for row in m_a:
        if type(row) is not list:
            raise TypeError("_a must be a list of lists")
        a = len(row)
        if b >= 0 and a != b:
            raise TypeError("each row of m_a must be of the same size")
        b = len(row)
        for ele in row:
            if type(ele) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
        list_length += 1

    # checking matrix is a matrix (2 or more than 2 list) or a simple list.
    if list_length < 2:
        raise TypeError("m_a can't be empty")


