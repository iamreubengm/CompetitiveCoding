#Minimum Window Substring
'''
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window.
If there is no such substring, return the empty string "".
The testcases will be generated such that the answer is unique.
A substring is a contiguous sequence of characters within the string.

Example:
    Input: s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"
    Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
'''

from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ''
        tc=Counter(t)
        chars=len(tc.keys())
        sc=Counter()
        matches=0
        res=''
        i=0
        j=-1
        while i<len(s):
            if matches<chars:
                if j==len(s)-1:
                    return res
                j+=1
                sc[s[j]]+=1
                if tc[s[j]]>0 and sc[s[j]]==tc[s[j]]:
                    matches+=1
            else:
                sc[s[i]]-=1
                if tc[s[i]]>0 and sc[s[i]]==tc[s[i]]-1:
                    matches-=1
                i+=1
            if matches==chars:
                if not res or (j-i+1)<len(res):
                    res=s[i:j+1]
        return res