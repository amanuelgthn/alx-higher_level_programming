#!/usr/bin/python3
def search_replace(my_list, search, replace):
    index = 0
    for i in my_list:
        if i == search:
            my_list[index] = replace
        index = index + 1
    return my_list
