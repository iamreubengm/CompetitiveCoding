#Consecutive Characters
'''
The power of the string is the maximum length of a non-empty substring that contains only one unique character.
Given a string s, return the power of s.

Example:
    Input: s = "leetcode"
    Output: 2
    Explanation: The substring "ee" is of length 2 with the character 'e' only.
'''

class Solution:
    def maxPower(self,s):
        count,res=1,1
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                count+=1
                res=max(res,count)
            else:
                count=1
        return res