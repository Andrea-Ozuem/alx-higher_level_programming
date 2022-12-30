#!/usr/bin/python3
""" Text Indentation module"""


def text_indentation(text):
    """prints a text with 2 new lines after each of these
       characters: ., ? and :
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    string = ""
    for c in text:
        string += c
        if c in '?.:':
            print(string.lstrip(), end='\n\n')
            string = ""
    print(string.lstrip(), end='')
