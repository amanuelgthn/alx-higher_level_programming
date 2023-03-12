#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    matrix_len = len(matrix)
    if matrix:
        for i in matrix:
            k = 0
            for j in i:
                print("{:d}".format(j), end="")
                k = k + 1
                if k != 3:
                    print(end=" ")
            print()
