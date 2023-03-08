#!/usr/bin/python3
def pow(a, b):
    i = 1
    if b < 0:
        b = -b
        a = 1 / a
    if b % 2 == 0:
        a = abs(a)
    while i < b:
        a = a * a
        i = i + 1
    return a
