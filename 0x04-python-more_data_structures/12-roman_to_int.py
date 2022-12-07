#!/usr/bin/python3
def roman_to_int(roman_string):
    if (not isinstance(roman_string, str)) or None:
        return 0
    symbol = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    for i in range(len(roman_string)):
        if roman_string[i] not in symbol:
            return 0

        num = symbol[roman_string[i]]
        if i != len(roman_string) - 1:
            next_c = symbol[roman_string[i + 1]]
        else:
            next_c = num

        if num >= next_c:
            total += num
        else:
            total -= num
    return total
