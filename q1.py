#! user/bin/env python
"""
q1.py - Euler Question No. 1

Question:
If we list all the natural numbers below 10 that are multiples 
of 3 or 5,
 we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""
def solveQ1(upper_limit):
    """
    It solves question 1
    """
    sum = 0
    for i in range(0, upper_limit):
        if i % 3 == 0 or i % 5 == 0:
            sum = sum+i
    if sum !=0:
        return sum
if __name__ == '__main__':
    print("Started Main Function")
    a = solveQ1(1000)
    print("Answer: %s" % a)
