#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argLength = len(sys.argv)
    argNumber = argLength - 1
    if argLength == 1:
        print("0 arguments.")
    else:
        if argLength == 2:
            print("{:d} argument:".format(argNumber))
        else:
            print("{:d} arguments:".format(argNumber))
        for i in range(1, argLength):
            print("{:d}: {:s}".format(i, sys.argv[i]))
