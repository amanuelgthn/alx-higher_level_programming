#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    x = 0
    for keys in a_dictionary.keys():
        x = a_dictionary[keys]
        a_dictionary[keys] = 2 * x
    return a_dictionary
