#Distinct Subsequences
'''
Given two strings s and t, return the number of distinct subsequences of s which equals t.
A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' relative positions.
i.e. "ACE" is a subsequence of "ABCDE" while "AEC" is not.
It is guaranteed the answer fits on a 32-bit signed integer.

Example:
    Input: s = "rabbbit", t = "rabbit"
    Output: 3
    Explanation:
        As shown below, there are 3 ways you can generate "rabbit" from S.
        rabb b it
        ra b bbit
        rab b bit
'''

class Solution:
    def numDistinct(self,s,t):
        n=len(s)
        m=len(t)
        d=[[0]*(m+1) for i in range(n+1)]
        for i in range(n+1):
            d[i][0]=1
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                d[i][j]+=d[i-1][j]
                if s[i-1]==t[j-1]:
                    d[i][j]+=d[i-1][j-1]
        return d[-1][-1]