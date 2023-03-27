#!/usr/bin/python3
def roman_to_int(roman_string):
    dict = {"I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000}
    keys = dict.keys()
    sum = 0
    length = len(roman_string)
    if(str(roman_string)):
        for i in range(1,length):
            str1 = roman_string[i-1]
            str2 = roman_string[i]
            if rom in dict:
                if dict[str1] > dict[str2]:
                    sum = sum + dict[str1]
                    print(dict[str1])
                else:
                     sum = sum - dict[str1]
            else:
                return 0
        return sum
    else:
        return 0
