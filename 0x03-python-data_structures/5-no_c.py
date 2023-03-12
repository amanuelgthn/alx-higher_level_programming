#!/usr/bin/python3
def no_c(my_string):
    str_len = len(my_string)
    new_str = ""
    for i in my_string:
        if i != 'C' and i != 'c':
            new_str = new_str + i
    return new_str
