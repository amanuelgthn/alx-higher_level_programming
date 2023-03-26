#!/usr/bin/python3
def roman_to_int(roman_string):
    dict = {"I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000}
    list = roman_string.split()
    sum = 0 
    for num in list:
        if num in dict:
           print(dict[num])
        else:
            return 0
    return sum
