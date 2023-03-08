#!/usr/bin/python3
def uppercase(str):
    len_str = len(str)
    i = 0
    while i < len_str:
        int_str = int(ord(str[i]))
        if (int_str > 96 and int_str < 123):
                      print("{}".format(chr(int_str-32)), end="")
        else:
                      print("{}".format(str[i]), end="")
        i = i + 1
