#Palindrome Partitioning II
'''
Given a string s, partition s such that every substring of the partition is a palindrome.
Return the minimum cuts needed for a palindrome partitioning of s.

Example:
Input: s = "aab"
    Output: 1
    Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
'''

from functools import lru_cache

class Solution:
    def minCut(self, s: str) -> int:
        n=len(s)
        
        @lru_cache(None)
        def isPal(l,r):
            if l>=r:
                return 1
            if s[l]!=s[r]:
                return 0
            return isPal(l+1,r-1)
        
        @lru_cache(None)
        def dp(i):
            if i==n:
                return 0
            res=float('inf')
            for j in range(i,n):
                if isPal(i,j):
                    res=min(res,dp(j+1)+1)
            return res
        return dp(0)-1