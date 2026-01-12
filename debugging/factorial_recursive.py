#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function description:
    This function calculates the factorial of a given number using recursion.
    The factorial of a number n is the product of all positive integers from 1 to n.
    By definition, the factorial of 0 is 1.

    Parameters:
    n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
    int: The factorial of the given number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Get the argument from the command line, convert it to an integer,
# compute its factorial and display the result.
f = factorial(int(sys.argv[1]))
print(f)
