#!/usr/bin/python3
def element_at(my_list, idx):
    len_list = len(my_list)
    if idx < 0 or idx >= len_list:
        return
    return my_list[idx]