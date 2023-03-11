#!/usr/bin/python3
def element_at(my_list, idx):
    len_list = len(my_list)
    if idx < 0 or idx > len_list:
        return
    element = my_list[idx]
    print("Element at index {} is {}".format(idx, element))
