#Ones and Zeroes
'''
You are given an array of binary strings strs and two integers m and n
Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.
A set x is a subset of a set y if all elements of x are also elements of y.

Example:
    Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
    Output: 4
    Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
                 Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
                 {"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.
'''

class Solution:
    def findMaxForm(self,strs,m,n):
        dp = [[0 for i in range(n+1)] for i in range(m+1)]
        for x in strs:
            zeros = x.count("0")
            ones = len(x) - zeros
            for i in range(m, zeros-1,-1):
                for j in range(n,ones-1,-1):
                    dp[i][j]=max(dp[i][j],dp[i-zeros][j-ones]+1)
        return dp[m][n]