#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
        last_digit = number % 10
else:
        last_digit = number % 10 - 10
str1 = "Last digit of "
str2 = " is "
str5 = " and is greater than 5"
str0 = " and is 0"
str6 = " and is less than 6 and not 0"
if last_digit > 5:
        print(f"{str1}{number}{str2}{last_digit}{str5}")
elif last_digit == 0:
        print(f"{str1}{number}{str2}{last_digit}{str0}")
else:
        print(f"{str1}{number}{str2}{last_digit}{str6}")
