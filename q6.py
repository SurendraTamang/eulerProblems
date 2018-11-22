#! user/bin/env python
"""
q6.py - Project Euler Question No. 6 - Sum square difference

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the
first ten natural numbers and the square of the
sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.

 Question Link:- https://projecteuler.net/problem=6
"""


def solveQ6(natural_number):
     """
    It solves question 6
    """
    square_sum = 0
    sum = 0
    for i in range(1, (natural_number+1)):
        square = i*i
        square_sum = square_sum+square
        sum = sum+i
    diff = (sum*sum) - square_sum
    if diff != 0:
        return diff


if __name__ == '__main__':
    print("Started Main Function")
    a = solveQ6(100)
    print("Answer: %s" % a)
