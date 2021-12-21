#Power of Two
'''
Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x.

Example:
    Input: n = 1
    Output: true
    Explanation: 2^0 = 1
'''

class Solution:
    def isPowerOfTwo(self,n):
        return n>0 and not (n&n-1)