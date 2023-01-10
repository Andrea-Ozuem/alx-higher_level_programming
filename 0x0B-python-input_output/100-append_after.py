#!/usr/bin/python3
"""Search and Update"""


def append_after(filename="", search_string="", new_string=""):
    """Appends newstr to file after search is found"""
    with open(filename, mode="r", encoding="utf-8") as f:
        buf = f.readlines()
        count = 0
        for row in buf:
            count += 1
            if search_string in row:
                buf.insert(count, new_string)
    with open(filename, mode="w", encoding="utf-8") as f:
        f.writelines(buf)
