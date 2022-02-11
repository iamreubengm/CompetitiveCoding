#Permutation in String
'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example:
    Input: s1 = "ab", s2 = "eidbaooo"
    Output: true
    Explanation: s2 contains one permutation of s1 ("ba").
'''

from collections import Counter

class Solution:
    def checkInclusion(self,s1,s2):
        c=Counter(s1)
        n=len(s1)
        for i in range(len(s2)):
            if s2[i] in c:
                c[s2[i]]-=1
            if i>=n and s2[i-n] in c:
                c[s2[i-n]]+=1
            if all(not c[x] for x in c):
                return True
        return False