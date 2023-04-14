#!/usr/bin/python3
"""
Module containing Pascal's Triangle
"""


def pascal_triangle(n):
    column = []
    for i in range(0,n):
        row = []
        for j in range(0,i):
            row.append(j)
        column.append(row)
    return column

