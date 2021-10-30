#Longest Duplicate Substring
'''
Given a string s, consider all duplicated substrings: (contiguous) substrings of s that occur 2 or more times. The occurrences may overlap.
Return any duplicated substring that has the longest possible length. If s does not have a duplicated substring, the answer is "".

Example:
    Input: s = "banana"
    Output: "ana"
'''

class Solution:
    def longestDupSubstring(self,s):
        res=''
        j=1
        for i in range(len(s)):
            longest=s[i:i+j]
            t=s[i+1:]
            while longest in t:
                res=longest
                j+=1
                longest=s[i:i+j]
        return res