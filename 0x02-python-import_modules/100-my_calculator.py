#!/usr/bin/python3
import sys

"""Executing the modules as scripts:
    by executing the module as the “main” file:
    """

if __name__ == "__main__":

    """importing functions from the file"""
    from calculator_1 import add, sub, mul, div

    """program conditional statement"""
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    """Available operators in the program"""
    signvar = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] not in list(signvar.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    """assign value to variables and casting arguments into integers"""
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    """printing the result"""
    print("{} {} {} = {}".format(a, sys.argv[2], b, signvar[sys.argv[2]](a, b)))
