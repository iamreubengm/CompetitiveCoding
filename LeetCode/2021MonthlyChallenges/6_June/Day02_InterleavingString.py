#Interleaving String
'''
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:
    s = s1 + s2 + ... + sn
    t = t1 + t2 + ... + tm
    |n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

Example:
    Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
    Output: true

    Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
    Output: false
'''

class Solution:
    def isInterleave(self,s1,s2,s3):
        l1,l2,l3=len(s1),len(s2),len(s3)
        if l1+l2!=l3:
            return False
        d=[[True for _ in range(l2+1)] for _ in range(l1+1)]
        
        for i in range(1,l1+1):
            d[i][0]=d[i-1][0] and s1[i-1]==s3[i-1]
        for i in range(1,l2+1):
            d[0][i]=d[0][i-1] and s2[i-1]==s3[i-1]
        for i in range(1,l1+1):
            for j in range(1,l2+1):
                d[i][j]=(d[i-1][j] and s1[i-1]==s3[i-1+j]) or (d[i][j-1] and s2[j-1]==s3[i-1+j])
        return d[-1][-1]