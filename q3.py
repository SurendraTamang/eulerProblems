#!/usr/bin/env python
"""
q3.py - Project Euler Question No. 3- Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

Question Link:- https://projecteuler.net/problem=3
Program Written By :- Surendra Tamang
"""


def solveQ3(number_asked):
    """
    It solves the question no :-3

    """
    answer = 1
    # number = 600851475143
    for i in range(2, number_asked):
        count = 0

        if number_asked % i == 0:
            print(i)
            for j in range(2, i):
                if i % j == 0:
                    count = count+1
            if count == 0:
                if(answer < i):
                    answer = i
                    # print(i)
    return answer


if __name__ == '__main__':
    print("Started Main Function")
    a = solveQ3(600851475143)
    print("Answer: %s" % a)
