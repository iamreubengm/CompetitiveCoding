#Longest Uncommon Subsequence II
'''
Given an array of strings strs, return the length of the longest uncommon subsequence between them. If the longest uncommon subsequence does not exist, return -1.
An uncommon subsequence between an array of strings is a string that is a subsequence of one string but not the others.
A subsequence of a string s is a string that can be obtained after deleting any number of characters from s.
For example, "abc" is a subsequence of "aebdc" because you can delete the underlined characters in "aebdc" to get "abc".
Other subsequences of "aebdc" include "aebdc", "aeb", and "" (empty string).

Example:
    Input: strs = ["aba","cdc","eae"]
    Output: 3
'''

class Solution:
    def findLUSlength(self,strs):
        def issub(s, t):
            t=iter(t)
            return all(c in t for c in s)
        for s in sorted(strs, key=len, reverse=True):
            if sum(issub(s,t) for t in strs)==1:
                return len(s)
        return -1