#!/usr/bin/python3
for decimal in range(0, 100):
    if decimal == 99:
        print("{}".format(decimal))
    else:
        print("{:02}".format(decimal), end=", ")
