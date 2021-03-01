#Divide Two Integers
'''
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
Return the quotient after dividing dividend by divisor.
The integer division should truncate toward zero, which means losing its fractional part.
For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit
signed integer range: [−231,  231 − 1].
For this problem, assume that your function returns 231 − 1 when the division result overflows.
 

Example:
    Input: dividend = 10, divisor = 3
    Output: 3
    Explanation: 10/3 = truncate(3.33333..) = 3.
'''

class Solution:
    def divide(self,dividend,divisor):
        res=0
        x,y=abs(dividend),abs(divisor)
        for i in range(32,-1,-1):
            if x>=(y<<i):
                x-=(y<<i)
                res+=(1<<i)
        if (dividend>0 and divisor<0) or (dividend<0 and divisor>0): 
            res=-res
        return min(2**31-1,max(-2**31,res))