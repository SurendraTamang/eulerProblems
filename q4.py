#!/usr/bin/env python
"""
q4.py - Project Euler Question No. 4- Largest palindrome product

A palindromic number reads the same both ways. The largest
palindrome made from the product of two 2-digit numbers is
9009 = 91 × 99.
Find the largest palindrome made from the product of two
3-digit numbers.

Question Link:- https://projecteuler.net/problem=4
Program Written By :- Surendra Tamang
"""


def solveQ4(digit_number):
     """
    It solves question 4
    """
    result = 0
    highest = 1
    for i in range((digit_number-1), 1, -1):
        for j in range((digit_number-1), 1, -1):
            product = i*j
            first_part = product
            mod = 0
            while product != 0:
                pro = product % 10
                mod = mod*10+pro
                product = int(product/10)
                second_part = mod
            if first_part == second_part:
                result = first_part
                if highest < result:
                    highest = result
    return highest


if __name__ == "__main__":
    print("Started the main function")
    a = solveQ4(1000)
    print("Answer: %s" % a)
