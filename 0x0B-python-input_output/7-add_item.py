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


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
try:
    filename = load_from_json_file(filename)
except (ValueError, FileNotFoundError):
    list_item = []
n = len(sys.argv)
for i in sys.argv[1:]:
    list_item.append(i)
save_to_json_file(list_item, filename)
