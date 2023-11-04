#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    [print("{:d}".format(row[i]), end=" ") if i < len(row) - 1 else
     print("{:d}".format(row[i]), end="\n")
     for row in matrix for i in range(len(row))]
    if matrix == [[]]:
        print()
