#!/usr/bin/python3
"""
This Module solves the N queens problem
for N greater than or equal to 4
"""


import sys
"""
Solution for the N queens problem
"""
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
