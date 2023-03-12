#!/usr/bin/python3
def multiple_returns(sentence):
    length = 0
    first_char = None
    if sentence:
        length = len(sentence)
        first_char = sentence[0]
    a = (length, first_char)
    return a
