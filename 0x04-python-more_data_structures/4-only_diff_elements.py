#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    x = set()
    for element in set_1:
        x.add(element)
    for element in set_2:
        x.add(element)
    list = []
    for element in x:
        list.append(element)
