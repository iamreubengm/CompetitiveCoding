#Longest Common Subsequence
'''
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
    For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Example:
    Input: text1 = "abcde", text2 = "ace" 
    Output: 3  
    Explanation: The longest common subsequence is "ace" and its length is 3.
'''

class Solution:
    def longestCommonSubsequence(self,text1,text2):
        dp=[[0 for i in range(len(text2)+1)] for j in range(len(text1)+1)]
        text1=" "+text1
        text2=" "+text2
        for i in range(1,len(text1)):
            for j in range(1,len(text2)):
                dp[i][j]=1+dp[i-1][j-1] if text1[i]==text2[j] else max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]