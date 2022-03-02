#Is Subsequence
'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters
without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example:
    Input: s = "abc", t = "ahbgdc"
    Output: true
'''

class Solution:
    def isSubsequence(self,s,t):
        m,n=0,0
        while m<len(s) and n<len(t):
            if s[m]==t[n]:
                m+=1
            n+=1
        return m==len(s)