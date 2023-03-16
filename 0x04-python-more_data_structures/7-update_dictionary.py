#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    key_values = {key:value}
    a_dictionary.update(key_values)
    return a_dictionary
