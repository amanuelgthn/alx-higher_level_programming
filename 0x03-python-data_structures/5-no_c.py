#!/usr/bin/python3
def no_c(my_string):
    str_len = len(my_string)
    new_str = ""
    for i in (0, str_len-1):
        if my_string[i] != 'c' or my_string[i] != 'C':
            continue
        new_str = new_str + my_string[i]
    return new_str
