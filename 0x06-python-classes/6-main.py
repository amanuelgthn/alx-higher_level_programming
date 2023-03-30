#!/usr/bin/python3
Square = __import__('6-square').Square

try:
    my_square = Square(3, "Position")
    print(type(my_square.position))
except Exception as e:
    print(e)
