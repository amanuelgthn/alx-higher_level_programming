def safe_print_list(my_list=[], x=0):
    num_print = 0
    for i in my_list:
        try:
            while num_print < x:
                print(i)
                num_print += 1
        except:
            break
    return num_print
