#!/usr/bin/python3
""" Read and Write to stdout"""


def read_file(filename=""):
    """Reads from filename and wrtes to stdout"""
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
