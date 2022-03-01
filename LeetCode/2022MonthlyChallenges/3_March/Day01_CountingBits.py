#Counting Bits
'''
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Example:
    Input: n = 2
    Output: [0,1,1]
    Explanation:
        0 --> 0
        1 --> 1
        2 --> 10
'''

class Solution:
    def countBits(self,n):
        res=[0]*(n+1)
        for i in range(1,n+1):
            res[i]=res[i>>1]+i%2
        return res