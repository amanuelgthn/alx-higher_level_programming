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
    length = len(roman_string)
    if(str(roman_string)):
        for i in range(1,length):
            if roman_string[i] in dict:
                if dict[roman_string[i-1]] > dict[roman_string[i]]:
                    sum = sum + dict[roman_string[i-1]]
                else:
                     sum = sum - dict[roman_string[i-1]]
            else:
                return 0
        return sum
    else:
        return 0
