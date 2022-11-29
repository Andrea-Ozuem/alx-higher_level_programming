#!/usr/bin/python3
def remove_char_at(str, n):
    for c in str:
        for i in range(len(str)):
            if i == n:
                new_str = str[:n] + str[n + 1:]
                return new_str
    return str
