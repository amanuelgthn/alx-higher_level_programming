#!/usr/bin/python3
def uppercase(str):
    len_str = len(str)
    i = 0
    while i < len_str:
        int_str = int(ord(str[i]))
        if (int_str > 96 and int_str < 123):
                      print("{}".format(char(int_str-32)))
        else:
                      print("{}".format(str[i]))
        i = i + 1
