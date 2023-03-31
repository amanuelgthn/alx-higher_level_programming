#!/usr/bin/python3
class Car:
    color = "White"

    def __init__(self, make):
        self.make = make

car1 = Car("Ford")
print(car1.make)
print(car1.color)
print(type(car1))
print(type(None))
print(type("he"))