#Delete Operation for Two Strings
'''
Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.
In one step, you can delete exactly one character in either string.

Example:

    Input: word1 = "sea", word2 = "eat"
    Output: 2
    Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

    Input: word1 = "leetcode", word2 = "etco"
    Output: 4
'''

class Solution:
    def minDistance(self,word1,word2):
        m,n=len(word1),len(word2)
        d=[[0]*(n+1) for _ in range(m+1)]
        for i,x in enumerate(word1):
            for j,y in enumerate(word2):
                d[i+1][j+1]= max(d[i][j+1],d[i+1][j],d[i][j]+(x==y))
        return m+n-2*d[-1][-1]