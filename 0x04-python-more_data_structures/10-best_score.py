#!/usr/bin/python3
def best_score(a_dictionary):
    x = 0
    y = 0
    Name = None
    if a_dictionary:
        if len(a_dictionary) != 0:
            for keys in a_dictionary.keys():
                y = a_dictionary[keys]
                if x < y:
                    x = y
                    Name = keys
    return Name
