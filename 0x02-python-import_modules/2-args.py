#!/usr/bin/python3
import sys

if len(sys.argv) == 0:
    print("0 arguments.")
else:    
    for i in range(1, len(sys.argv)):
        if len(sys.argv) == 1:
            print(len(sys.argv), "argument:")
        else:
            print(len(sys.argv), "arguments:")  
        print(i, sys.argv[i])
