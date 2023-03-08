#!/usr/bin/python3
def uppercase(str):
    len_str = len(str)
    i = 0
    while i < len_str:
        int_str = int(ord(str[i]))
        if (int_str > 96 and int_str < 123):
            int_str = int_str - 32
        print("{}".format(chr(int_str)), end="")
        i = i + 1
     print()
