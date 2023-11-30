#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv)
    if length == 0:
        print("0 argument.")
    elif length == 1:
        for i in argv:
            print("{:d} argument:".format(length))
            print("{:d}: {:c}".format(length, i))
    else:
        for a in argv[1:]:
            print("{:d} argument:".format(length))
            print("{:d}: {:s}".format(length, a))
