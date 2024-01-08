#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv, exit


if __name__ == '__main__':
    n = len(argv) - 1

    if n != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])

    if operator not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == '*':
        result = mul(a, b)
    elif operator == '/':
        result = div(a, b)
    print("{} {} {} = {}".format(argv[1], argv[2], argv[3], result))