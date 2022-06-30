#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argLength = len(sys.argv)
    if argLength == 1:
        print("0 arguments.")
    else:    
        if argLength == 2:
            print((argLength - 1), "argument:")
        else:
            print((argLength - 1), "arguments:")      
        for i in range(1, len(sys.argv)):
            print("{:d}:".format(i) , sys.argv[i])
