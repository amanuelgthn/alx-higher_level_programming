#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv)
    print("{} arguments".format(n - 1), end="")
    if ( n == 1):
        print(".")
    else:
        print(":")
    for i in range(1, n):
        print("{}: {}".format(i, sys.argv[i]))
