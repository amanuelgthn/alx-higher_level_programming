#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (RuntimeError, TypeError, NameError, ValueError):
        sys.stderr.write("ValueError")
        return False
    else:
        return True
