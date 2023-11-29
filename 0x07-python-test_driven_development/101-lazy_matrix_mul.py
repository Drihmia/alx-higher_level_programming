#!/usr/bin/python3
from numpy import dot

"""
this module contains one funtion that multiplies 2 matrices by
using the module NumPy

"""


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        list of lists: The resulting matrix.

     Raises:
        TypeError: If m_a or m_b is not a list, or if m_a or m_b contains
            elements that are not lists.
        ValueError: If m_a or m_b is empty, if rows in m_a or m_b have
            different sizes, or if m_a and m_b cannot be multiplied.
    >>> matrix_mul([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]])
    [[58, 64], [139, 154]]

    """
    # checking the matrix.
    list_length = 0
    b = -9
    # matrix a
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")

    # matrix b
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    # looping through the outer list of m_a.
    for row in m_a:
        if type(row) is not list:
            raise TypeError("m_a must be a list of lists")
        len_row_a = len(row)

        if not len_row_a:
            raise ValueError("m_a can't be empty")
        # check if current row and previous  row has same size
        if b >= 0 and len_row_a != b:
            raise TypeError("each row of m_a must be of the same size")
        b = len_row_a
        for ele in row:
            if type(ele) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
        list_length += 1

    # checking matrix is a matrix (2 or more than 2 list) or a simple list.
    if list_length < 1:
        raise ValueError("m_a can't be empty")

    #################################################################
    # checking the matrix.
    list_length = 0
    b = -9
    # looping through the outer list of m_b.
    for row in m_b:
        if type(row) is not list:
            raise TypeError("m_b must be a list of lists")
        len_row_a = len(row)

        if not len_row_a:
            raise ValueError("m_b can't be empty")
        # check if current row and previous  row has same size
        if b >= 0 and len_row_a != b:
            raise TypeError("each row of m_b must be of the same size")
        b = len_row_a
        for ele in row:
            if type(ele) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")
        list_length += 1

    # checking matrix is a matrix (2 or more than 2 list) or a simple list.
    if list_length < 1:
        raise ValueError("m_b can't be empty")

    # check if m_a and m_b can't be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    return dot(m_a, m_b)
