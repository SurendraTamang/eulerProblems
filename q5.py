#! user/bin/env python
"""
q5.py - Project Euler Question No. 5 - Smallest multiple
Question:
2520 is the smallest number that can be divided by each
of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly
divisible by all of the numbers from 1 to 20?

Question Link:- https://projecteuler.net/problem=5
Program Written By :- Surendra Tamang

"""


def solveQ5(upper, step):
    """
    solves q5
    Here upper is for the up to which number we want divisible
    Step:- we took the HCF 20,19,18 for fast calculation
    """
    i = step
    while True:
        count = 0
        print(i)
        for j in range(1, (upper+1)):
            if i % j == 0:
                count += 1
        if count == upper:
            return i
        i += step


if __name__ == '__main__':
    print("Started Main Function")
    a = solveQ5(20, 3420)
    print("Answer: %s" % a)
