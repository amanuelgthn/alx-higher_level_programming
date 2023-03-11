#!/usr/bin/python3
if __name__ == "__main__":
    def print_list_integer(my_list=[]):
        list_len = len(my_list)
        for i in (0, list_len):
            print("{}".format(my_list[i]))
