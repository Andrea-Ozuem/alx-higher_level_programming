#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import mul, add, sub, div
    from sys import argv
    if (len(argv)) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operators = ["+", "-", "*", "/"]
    if argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    if argv[2] == "+":
        result = add(a, b)
    elif argv[2] == "-":
        result = sub(a, b)
    elif argv[2] == "*":
        result = mul(a, b)
    elif argv[2] == "/":
        result = div(a, b)
print("{} {} {} = {}".format(a, argv[2], b, result))
