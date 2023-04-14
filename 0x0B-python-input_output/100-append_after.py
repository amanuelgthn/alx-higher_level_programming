#!/usr/bin/python3
"""
module containing append_after function
"""


def append_after(filename="", search_string="", new_string=""):
    """
    function that inserts a line of text to a file,
    after each line containing a specific string
    """
    with open(filename, 'r', encoding="utf-8") as file:
        new_str = ""
        for line in file:
            if line.find(search_string) != -1:
                new_str += line + new_string
            else:
                new_str += line
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(new_str)
