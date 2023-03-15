#!/usr/bin/python3
def common_elements(set_1, set_2):
    list = []
    for val in set_1:
        for element in set_2:
            if val == element:
                list.append(val)
    return list


def only_diff_elements(set_1, set_2):
    list = common_elements(set_1, set_2)
    x = set()
    for element in set_1:
        if element not in list:
            x.add(element)
    for element in set_2:
        if element not in list:
            x.add(element)
    return x
