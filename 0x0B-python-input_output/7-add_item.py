#!/usr/bin/python3
"""
import sys Module
"""


import sys
"""
module containing a script that adds
arguments to a python list, and then
save them to a file
"""


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
    
    filename = "add_item.json"
    filename = load_from_json_file(filename)
    n = len(sys.argv)
    list = []
    list.extend(sys.argv[1:])
    save_to_json_file(list, filename)
    
