#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    nl = []
    for i in range(0, list_length):
        try:
            res = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            res = 0
            print("dividion by 0")
        except TypeError:
            res = 0
            print("wrong type")
        except IndexError:
            res = 0
            print("out of range")
        finally:
            nl.append(res)
    return nl
