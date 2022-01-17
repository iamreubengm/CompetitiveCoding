#Word Pattern
'''
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example:
    Input: pattern = "abba", s = "dog cat cat dog"
    Output: true
'''

class Solution:
    def wordPattern(self,pattern,s):
        d={}
        s=s.split(' ')
        if len(pattern)!=len(s) or len(set(pattern))!=len(set(s)):
            return False
        for i,x in enumerate(pattern):
            if x not in d:
                d[x]=s[i]
            elif d[x]!=s[i]:
                return False
        return True