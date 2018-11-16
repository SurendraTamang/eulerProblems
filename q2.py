#!/usr/bin/env python
"""
q2.py - Euler Question No. 2- Even Fibonacci numbers

Question:
Each new term in the Fibonacci sequence is generated 
by adding the previous two terms. By starting with 
1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence 
whose values do not exceed four million, 
find the sum of the even-valued terms.

Question Link https://projecteuler.net/problem=2

"""


def solveQ2(limit):
    a = 1
    b = 2
    sum = b
    while b < limit:
        c = a + b
        a = b
        b = c
        if c % 2 == 0:
            sum = sum + c

    return sum


# 4613732
if __name__ == '__main__':
    print("Started Main Function")
    a = solveQ2(4000000)
    print("Answer: %s" % a)
