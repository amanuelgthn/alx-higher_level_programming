#!/usr/bin/python3
"""
import json module
import sys
"""


import json
import sys
"""
module containing a script that adds
arguments to a python list, and then
save them to a file
"""


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

n = len(sys.argv)
list = []
for i in range(1, n):
    list.append(sys.argv[i])
filename = "add_item.json"
try:
    filename = load_from_json_file(filename)
except (FileNotFoundError):
    pass
save_to_json_file(list, filename)
