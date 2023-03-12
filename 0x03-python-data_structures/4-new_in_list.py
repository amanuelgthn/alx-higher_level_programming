#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    len_list = len(my_list)
    if idx < 0 or idx >= len_list:
        new_list = my_list.copy
        return new_list
    new_list = my_list.copy
    new_list[idx] = element
    return new_list
