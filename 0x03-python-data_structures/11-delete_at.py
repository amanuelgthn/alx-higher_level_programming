#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    list_len = len(my_list)
    if idx >= 0 and my_list and idx < list_len:
        del my_list[idx]
    return my_list
