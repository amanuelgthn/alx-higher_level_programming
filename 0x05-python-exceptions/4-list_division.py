#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = 0
    a = 0
    b = 0
    len1 = len (my_list_1)
    len2 = len (my_list_2)
    index = len1
    if index < len2:
        index = len2
    for i in range(0, index):
        
    try:
        result = a / b
        print("Inside result: {:d}".format(result))
    except ZeroDivisionError:
        pass
    finally:
        return 
