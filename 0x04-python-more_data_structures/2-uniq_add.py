#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    unique = set(my_list)
    for element in unique:
        sum = sum + element
    return sum
