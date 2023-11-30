#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv) - 1
    if length == 0:
        print("0 arguments.")
    elif length == 1:
        print("1 argument:")
        print("1: {:s}".format(argv[1]))
    elif length > 1:
        print("{:d} arguments:".format(length - 1))
        for i in range(1, length):
            print("{:d}: {:s}".format(i, argv[i]))
