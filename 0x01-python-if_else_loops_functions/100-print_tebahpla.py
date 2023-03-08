#!/usr/bin/python3
i = 122
while i > 64:
    upper = 0
    if i % 2 != 0:
        upper = 32
    print("{}".format(chr(i - upper)), end="")
