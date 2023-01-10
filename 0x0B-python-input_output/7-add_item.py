#!/usr/bin/python3
"""a script that adds all arguments to a Python list
   and then save them to a file
"""

from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

file_n = "add_item.json"
try:
    curr = load_from_json_file(file_n)
except FileNotFoundError:
    curr = []

for i in range(1, len(argv)):
    curr.append(argv[i])
save_to_json_file(curr, file_n)
