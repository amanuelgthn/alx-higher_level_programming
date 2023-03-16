#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    x = 0
    if len(a_dictionary) != 0:
        for keys in a_dictionary.keys():
            x = a_dictionary[keys]
            a_dictionary[keys] = int(2 * x)
    return a_dictionary
