#Perfect Squares
'''
Given an integer n, return the least number of perfect square numbers that sum to n.
A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.
For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

Example:
    Input: n = 12
    Output: 3
    Explanation: 12 = 4 + 4 + 4.
'''

class Solution:
    def numSquares(self,n):
        dp=[0]+[float('inf')]*n
        for i in range(1,n+1):
            for j in range(1,int(i**0.5)+1):
                dp[i]=min(dp[i],dp[i-j*j])
            dp[i]+=1
        return dp[i]