#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    x = 0
    dict = {}
    if len(a_dictionary) != 0:
        for keys in a_dictionary.keys():
            x = a_dictionary[keys]
            dict[keys] = int(2 * x)
    return dict
