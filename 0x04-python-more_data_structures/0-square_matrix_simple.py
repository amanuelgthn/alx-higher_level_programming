#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    list=[]
    for row in matrix:
        column = []
        for i in range(0,len(row)):
            column.append(row[i]*row[i])
        list.append(column)
    return list
