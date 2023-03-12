#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    matrix_len = len(matrix)
    if matrix:
        for i in matrix:
            for j in (0, 3):
                print("{:d}".format(i[j]), end="")
                if j != 2:
                    print(end=" ")      
            print()
