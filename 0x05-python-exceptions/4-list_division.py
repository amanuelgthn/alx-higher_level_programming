#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = 0
    list=[]
    a = 0
    b = 0
    result = 0
    len1 = len (my_list_1)
    len2 = len (my_list_2)
    index = len1
    if index < len2:
        index = len2
    while i < index && j < index:
        try:
            a = my_list_1[i]
            i+=1
        except:
            pass
        try:
            b = my_list_2[i]
        except:
            pass
        try:
            result = a / b
            list.append(result)
            list_length += 1
        except:
            pass
    return list         
