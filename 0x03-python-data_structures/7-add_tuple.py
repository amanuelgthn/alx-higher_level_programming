#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a[0]:
        num1 = tuple_a[0]
    else:
        num1 = 0
    if tuple_a[1]:
        num2 = tuple_a[1]
    else:
        num2 = 0
    if tuple_b[0]:
        num3 = tuple_b[0]
    else:
        num3 = 0
    if tuple_b[1]:
        num4 = tuple_b[1]
    else:
        num4 = 0
    
    c = num1 + num3
    d = num2 + num4
    tuple_add = (c, d)
    return tuple_add
