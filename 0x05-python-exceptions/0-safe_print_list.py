#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num_print = 0
    for i in my_list:
        try:
            if num_print < x:
                print("{}".format(i), end="")
                num_print += 1
        except:
            break
    print()
    return num_print
