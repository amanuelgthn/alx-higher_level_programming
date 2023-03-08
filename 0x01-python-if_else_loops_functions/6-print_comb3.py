#!/usr/bin/python3
for decimal in range(0, 100):
    last_digit = decimal % 10
    tens_digit = decimal / 10
    if decimal == 89:
        print("{}".format(decimal))
    elif last_digit > tens_digit:
        print("{:02}".format(decimal), end=", ")
