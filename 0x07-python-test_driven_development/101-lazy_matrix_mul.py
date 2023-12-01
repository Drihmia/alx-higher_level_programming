#!/usr/bin/python3
"""
this module contains one funtion that multiplies 2 matrices by
using the module NumPy

>>> lazy_matrix_mul([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]])
array([[ 58,  64],
       [139, 154]])
"""
from numpy import matmul


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
    >>> lazy_matrix_mul([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]])
    array([[ 58,  64],
           [139, 154]])

    """
    return matmul(m_a, m_b)
