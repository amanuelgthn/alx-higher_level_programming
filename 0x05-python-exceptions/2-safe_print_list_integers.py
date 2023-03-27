#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num_print = 0
    for i in my_list:
        try:
            if num_print < x:
                print("{:d}".format(i), end="")
                num_print += 1
        except (RuntimeError, TypeError, NameError, ValueError, IndexError):
            pass
    print()
    return num_print
