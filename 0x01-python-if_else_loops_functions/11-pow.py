#!/usr/bin/python3
def pow(a, b):
    i = 1
    if b % 2 == 0 and a < 0:
        a = -a
    if b < 0:
        b = -b
        a = 1 / a
    while i < b:
        a = a * a
        i = i + 1
    return a
