#!/usr/bin/python3
"""
Module containing a function that divides all elements of a matrix
matrix must be a list of integers or floats
div must be a number(integer or float) and can't be equalt to 0
raise TypeError or ZeroDivisionError for the conditions respectively
"""


def matrix_divided(matrix, div):
    """
    function that divides all elements of a matrix
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if matrix:
        if type(matrix[0]) != list:
            raise TypeError("matrix must be a matrix"
                            " (list of lists) of integers/floats")
        len_row = len(matrix[0])
        for row in matrix:
            if type(row) != list:
                raise TypeError("matrix must be a matrix"
                                " (list of lists) of integers/floats")
            elif len(row) != len_row:
                raise TypeError("Each row of the matrix"
                                " must have the same size")
            for i in row:
                if type(i) not in [int, float]:
                    raise TypeError("matrix must be a matrix"
                                    " (list of lists) of integers/floats")
    else:
        raise TypeError("matrix must be a matrix" 
                        " (list of lists) of integers/floats")
    new = []
    for row in matrix:
        column = []
        for i in range(0, len_row):
            column.append(round(row[i] / div, 2))
        new.append(column)
    return new
