#Fibonacci Number
'''
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

Example:
    Input: n = 2
    Output: 1
    Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Solution:
There are several ways to solve this, including recursion. But a space saving iterative approach
stores the last two numbers at every instance, calculates the next and replaces as necessary. Finally
the last number in the list is returned.
'''

class Solution:
    def fib(self,n):
        if n==0:
            return 0
        f=[0,1]
        for i in range(2,n+1):
            f=[f[-1],f[-1]+f[-2]]
        return f[-1]