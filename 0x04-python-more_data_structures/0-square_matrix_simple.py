#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    k =0
    list=[]
    for row in matrix:
        column = []
        for i in range(0,3):
            column.append(row[i]*row[i])
        list.append(column)
    return list
