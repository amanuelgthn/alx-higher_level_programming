#!/usr/bin/python3
def roman_to_int(roman_string):
    dict = {"I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000}
    sum = 0
    if(str(roman_string)):
        for num in roman_string:
            if num in dict:
                sum = sum + dict[num]
            else:
                return 0
        return sum
    else:
        return 0
