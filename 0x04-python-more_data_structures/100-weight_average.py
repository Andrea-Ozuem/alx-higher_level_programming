#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    nl = [x * y for i in my_list for x, y in i]
        
