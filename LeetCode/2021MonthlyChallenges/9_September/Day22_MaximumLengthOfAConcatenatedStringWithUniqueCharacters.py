#Maximum Length of a Concatenated String with Unique Characters
'''
Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.
Return the maximum possible length of s.

Example:
    Input: arr = ["un","iq","ue"]
    Output: 4
    Explanation:
        All possible concatenations are "","un","iq","ue","uniq" and "ique".
        Maximum length is 4.
'''

class Solution:
    def maxLength(self,arr):
        res=0
        u=['']
        
        for x in arr:
            for i in u:
                t=x+i
                if len(t)==len(set(t)):
                    u.append(t)
                    res=max(res,len(t))
        return res