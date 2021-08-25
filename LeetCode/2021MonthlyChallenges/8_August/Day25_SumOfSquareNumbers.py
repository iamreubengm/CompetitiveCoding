#Sum of Square Numbers
'''
Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

Example:
    Input: c = 5
    Output: true
    Explanation: 1 * 1 + 2 * 2 = 5
'''

import math

class Solution:
    def judgeSquareSum(self,c):
        squares=set()
        for i in range(int(math.sqrt(c))+1):
            squares.add(i**2)
        for a in squares:
            if c-a in squares:
                return True
        return False