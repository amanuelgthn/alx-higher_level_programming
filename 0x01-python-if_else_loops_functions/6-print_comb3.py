#!/usr/bin/python3
for decimal in range(0, 10):
    for last_digit in range(0, 10):
        if(last_digit > decimal):
             print("{}".format(decimal),end="")
             print("{}, ".format(last_digit),end="")
