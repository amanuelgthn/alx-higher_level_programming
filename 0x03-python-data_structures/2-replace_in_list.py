#!/usr//bin/python3
def replace_in_list(my_list, idx, element):
    len_list = len(my_list)
    if idx < 0 or idx > len_list:
        return None
    if idx > len_list:
        return my_list
    else:
        my_list[idx] = element
        return my_list
