#Arranging Coins
'''
You have n coins and you want to build a staircase with these coins.
The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.
Given the integer n, return the number of complete rows of the staircase you will build.

Example:
    Input: n = 5
    Output: 2
    Explanation: Because the 3rd row is incomplete, we return 2.
'''

from math import sqrt

class Solution:
    def arrangeCoins(self,n):
        return int((-1+(sqrt(1+8*n)))//2)

    def arrangeCoins2(self, n: int) -> int:
        l,h=1,n
        while l<=h:
            m=(l+h)//2
            t=(m*(m+1))//2
            if t==n:
                return m
            elif t>n:
                h=m-1
            else:
                l=m+1
        return h