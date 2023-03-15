#!/usr/bin/python3
def common_elements(set_1, set_2):
    list = []
    for val in set_1:
        for element in set_2:
            if val == element:
                list.append(val)
    return list
