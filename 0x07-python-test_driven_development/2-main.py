#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
test1 = [[1, 2, 3, 4, 6, 7, 8],[4, 5, 6, 8, 6, 7, 6],[3, 4, 5, 9, 8, 9, 10]]
test2 = [[1, 2, 3, 4, 6, 7, 8],
         [4, 5, 6, 8, 6, 7, 6],
         [3, 4, 5, "l", 8, "9", 10]]
print(matrix_divided(test1,float("inf")))
print(test1)
