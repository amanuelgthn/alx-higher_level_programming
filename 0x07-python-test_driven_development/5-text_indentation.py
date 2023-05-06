#!/usr/bin/python3
"""
This is a module containing text_indentaion function
"""

def split_text(text, symbol):
    """
    function that returns a list of split text with the given symbols
    """
    result =[]
    curr_char = ""
    for char in text:
        if char in symbol:
            if curr_char:
                result.append(curr_char+char)
                curr_char = ""
        else:
            if char == " " and curr_char == "":
                continue
            else:
                curr_char += char
    if curr_char:
        result.append(curr_char)
    return result

def text_indentation(text):
    """
    Function that prints a text with 2 new lines after each 
    these characters: ., ? and :
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    else:
        list_split = []
        list_split = split_text(text, ["." , ":" , "?"])
        for item in list_split:
            print(item)
