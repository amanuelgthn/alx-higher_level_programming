#!/usr/bin/python3
def no_c(my_string):
    str_len = len(my_string)
    new_str = ""
    for i in (0,str_len):
        if i != 'c' or i != 'C':
            new_str = new_str + i
    return new_str
