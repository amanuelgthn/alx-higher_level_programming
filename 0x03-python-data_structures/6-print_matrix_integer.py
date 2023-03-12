#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix = [[]]:
        print()
    if matrix:
        for i in matrix:
            k = 0
            if i:
                str_len = len(i)
                for j in i:
                    print("{:d}".format(j), end="")
                    k = k + 1
                    if k != str_len:
                        print(end=" ")
                print()
