#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    k =0
    list=[[]]
    for i in matrix:
        for j in i:
            list[k].append(j*j)
        k = k + 1
    return list
