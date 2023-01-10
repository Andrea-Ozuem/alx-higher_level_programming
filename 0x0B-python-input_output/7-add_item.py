#!/usr/bin/python3
"""a script that adds all arguments to a Python list
   and then save them to a file
"""

from sys import argv
from os.path import exists
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

file_n = "add_item.json"
py_list = []

if not exists(file_n):
    with open(file_n, "w", encoding="utf-8") as f:
        pass

curr = load_from_json_file(file_n)
for item in curr:
    py_list.append(item)

for i in range(1, len(argv)):
    py_list.append(argv[i])
save_to_json_file(py_list, file_n)
