#!/usr/bin/python3
def remove_char_at(str, n):
    str_len = len(str)
    str2=[]
    i = 0
    j = 0
    while(i < str_len and n >= 0 and n < str_len):
        if i != n:
            str2.append(str[i])
        i = i + 1
        j = j + 1
    if n >= 0 and n < str_len:
        return join(str2)
    else:
        return str
