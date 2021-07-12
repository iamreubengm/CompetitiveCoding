#Isomorphic Strings
'''
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.

Example:
    Input: s = "egg", t = "add"
    Output: true

    Input: s = "foo", t = "bar"
    Output: false
'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def helper(s):
            d={}
            res=''
            nxt='a'
            for x in s:
                if x not in d:
                    d[x]=nxt
                    nxt=chr(ord(nxt)+1)
                res+=d[x]
            return res
        return helper(s)==helper(t)