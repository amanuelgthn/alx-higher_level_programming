#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    matrix_len = len(matrix)
    if matrix:
        for i in matrix:
            k = len(i)
            for j in (0, k):
                print("{:d}".format(i[j]), end="")
                if j != k -1
                    print(end=" ")      
            print()
