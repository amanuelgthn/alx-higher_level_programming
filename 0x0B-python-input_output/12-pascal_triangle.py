#!/usr/bin/python3
"""
Module containing Pascal's Triangle
"""


def factorial_num(n):
    """
    function that returns the factorial of a number
    """
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * factorial_num(n-1)


def combination(col, row):
    """
    function that returns the combination of two numbers
    """
    return int(factorial_num(col) /
               factorial_num(row) / factorial_num(col - row))


def pascal_triangle(n):
    """
    function that returns the list of pascal triangle coefficients
    """
    column = []
    if n <= 0:
        return column
    for i in range(1, n+1):
        row = []
        for j in range(0, i):
            value = combination(i-1, j)
            row.append(value)
        column.append(row)
    return column
