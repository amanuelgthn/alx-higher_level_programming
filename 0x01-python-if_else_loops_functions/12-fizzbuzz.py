#!/usr/bin/python3
def fizzbuzz():
    for decimal in range(1, 101):
        if decimal % 3 == 0 and decimal % 5 == 0:
            print("FizzBuzz", end="")
        elif decimal % 3 == 0:
            print("Fizz", end="")
        elif decimal % 5 == 0:
            print("Buzz", end="")
        else:
            print("{}".format(decimal), end="")
        print(" ", end="")
