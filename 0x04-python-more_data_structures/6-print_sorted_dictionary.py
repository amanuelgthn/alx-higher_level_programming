#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list = sort(a_dictionary.keys())
    for i in list:
        print (i, a_dictionary[i])
