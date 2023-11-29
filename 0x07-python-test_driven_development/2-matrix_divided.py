#!/usr/bin/python3
"""
this module contains one funtion that divides all elements of a matrix.

>>> matrix = [
...     [1, 2, 3],
...     [4, 5, 6]
... ]
>>> type(matrix)
<class 'list'>
>>> type(matrix[0])
<class 'list'>
>>> matrix_divided(matrix, 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
>>> div = 9
>>> type(div)
<class 'int'>
>>> div = 9.8
>>> type(div)
<class 'float'>

"""


def matrix_divided(matrix, div):
    """Return a new matrix

    Matrix must be a list of lists of integers or floats.
    Each row of the matrix must be of the same size.
    div must be a number (integer or float).
    div can’t be equal to 0.
    All elements of the matrix will be divided by div,
        and rounded to 2 decimal places

    >>> matrix = [
    ...     [1, 2, 3],
    ...     [4, 5, 6]
    ... ]
    >>> matrix_divided(matrix, 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    >>> matrix
    [[1, 2, 3], [4, 5, 6]]

    >>> matrix_divided(matrix, 0)
    Traceback (most recent call last):
    ZeroDivisionError: division by zero
    >>> matrix
    [[1, 2, 3], [4, 5, 6]]

    >>> matrix_divided(matrix, "string")
    Traceback (most recent call last):
    TypeError: div must be a number
    >>> matrix
    [[1, 2, 3], [4, 5, 6]]

    >>> matrix = [
    ...     [1, "Red", 3],
    ...     [4, 5, 6]
    ... ]
    >>> matrix_divided(matrix, 3)
    Traceback (most recent call last):
    TypeError: matrix must be a matrix (list of lists) of integers/floats
    >>> matrix
    [[1, 'Red', 3], [4, 5, 6]]
    >>> matrix = [1, 2, 3, 4, 5, 6]
    >>> matrix_divided(matrix, 3)
    Traceback (most recent call last):
    TypeError: matrix must be a matrix (list of lists) of integers/floats
    >>> matrix
    [1, 2, 3, 4, 5, 6]
    >>> matrix = [
    ...     [1, 2],
    ...     [4, 5, 6]
    ... ]
    >>> matrix_divided(matrix, 3)
    Traceback (most recent call last):
    TypeError: Each row of the matrix must have the same size
    >>> matrix
    [[1, 2], [4, 5, 6]]
    >>> matrix = [
    ...     [1, 2, 3],
    ...     [4, 5]
    ... ]
    >>> matrix_divided(matrix, 3)
    Traceback (most recent call last):
    TypeError: Each row of the matrix must have the same size
    >>> matrix
    [[1, 2, 3], [4, 5]]
    >>> matrix = [[]]
    >>> matrix_divided(matrix, 2)
    Traceback (most recent call last):
    TypeError: matrix must be a matrix (list of lists) of integers/floats
    >>> matrix = []
    >>> matrix_divided(matrix, 2)
    Traceback (most recent call last):
    TypeError: matrix must be a matrix (list of lists) of integers/floats

    """

    # checking the parameter div.
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # checking the matrix.
    list_length = 0
    b = -9
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    # looping through the outer list of matrix.
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
        a = len(row)
        if b >= 0 and a != b:
            raise TypeError("Each row of the matrix must have the same size")
        b = len(row)
        for ele in row:
            if type(ele) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
        list_length += 1

    # checking matrix is a matrix (2 or more than 2 list) or a simple list.
    if list_length < 2:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    # creating new matrix, the result of dividing the original matrix by div.
    new_matrix = []
    for row in matrix:
        tmp = []
        for ele in row:
            tmp.append(round(ele / div, 2))
        new_matrix.append(tmp)
    return new_matrix


if __name__ == "__main__":
    import doctest
    flags = doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS | doctest.FAIL_FAST
    doctest.testmod(optionflags=flags)
