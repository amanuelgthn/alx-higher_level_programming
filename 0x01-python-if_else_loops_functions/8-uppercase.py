#!/usr/bin/python3
def uppercase(str):
    len_str = len(str)
    for i in range(0,len):
        if ord(str[i]) > 96 and ord(str[i]) < 123:
            print("{}".format(char(ord(str[i]) -32)))
        else:
            print("{}".format(str[i]))
            
