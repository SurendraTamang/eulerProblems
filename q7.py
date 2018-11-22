#!/usr/bin/env python
"""
q7.py - Project Euler Question No. 7- 10001st prime

By listing the first six prime numbers: 2, 3, 5,
7, 11, and 13,
we can see that the 6th prime is 13.
What is the 10 001st prime number?

Question Link:- https://projecteuler.net/problem=7

Program Written By :- Surendra Tamang
"""


def solveQ7(position):
    """
    It solves question 7
    """

    i = 3

    prime_count = 1
    while True:
        count = 0

        for j in range(2, i):
            if i % j == 0:
                count = count+1
        if count == 0:
            print(i)
            prime_count = prime_count + 1
        if prime_count == 1:
            return 2
        if prime_count == (position):
            return i
        i = i+1


if __name__ == '__main__':
    print("Started the main function")
    a = solveQ7(10001)
    print("Answer: %s " % a)
