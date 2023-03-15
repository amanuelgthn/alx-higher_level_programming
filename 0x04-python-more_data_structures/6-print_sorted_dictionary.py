#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_keys = []
    list_keys = list(a_dictionary.keys())
    list.sort()
    for i in list_keys:
        print (i, a_dictionary[i])
