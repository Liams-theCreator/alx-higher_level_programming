#!/usr/bin/python3
if __name__ == "__main__":
    from calcul import add, sub, div, mul
    from sys import argv, exit

    length = len(argv)
    if length != 4:
        exit(1)

    a = int(argv[1])
    operater = argv[2]
    b = int(argv[3])

    if operater == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif operater == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif operater == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif operater == "/":
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
