#! user/bin/env python
"""
q5.py - Euler Question No. 5

Question:
2520 is the smallest number that can be divided by each
of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly
divisible by all of the numbers from 1 to 20?

"""

def solveQ5(upper):
    """
    solves q5
    """
    i = 40
    while True:
        count = 0
        print(i)
        for j in range(1, (upper+1)):
            if i % j == 0:
                count += 1
        if count==upper:
            return i
        i += upper
        
if __name__ == '__main__':
    print("Started Main Function")
    a = solveQ5(20)
    print("Answer: %s" % a)
