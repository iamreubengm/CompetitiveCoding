#Nth Magical Number
'''
A positive integer is magical if it is divisible by either a or b.
Given the three integers n, a, and b, return the nth magical number. Since the answer may be very large, return it modulo 109 + 7.

Example:
    Input: n = 1, a = 2, b = 3
    Output: 2
'''

from math import gcd

class Solution:
    def nthMagicalNumber(self,n,a,b):
        lcm=(a*b)//gcd(a,b)
        l,r=0,n*min(a,b)
        while l<r:
            m=(l+r)//2
            if m//a+m//b-m//lcm<n:
                l=m+1
            else:
                r=m
        return l%(10**9+7)