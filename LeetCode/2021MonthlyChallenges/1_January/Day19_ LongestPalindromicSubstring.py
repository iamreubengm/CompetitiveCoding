#Longest Palindromic Substring
'''
Given a string s, return the longest palindromic substring in s.
Example:
    Input: s = "babad"
    Output: "bab"
    Note: "aba" is also a valid answer.
    
Solution:
The palindromic substrings can be of odd or even lengths(checkpal (i,i)/(i,i+1).
Thus we take the middle character and move outward till we get different characters. 
The checkpal function does this and returns the indices.
If the length of the substring is greater than the current max length, it is replaced
and the indices are stored. Finally the substring is returned.
'''

class Solution:
    def longestPalindrome(self,s):
        maxlen=0
        r=0
        l=0
        for i in range(len(s)):
            l1,r1=self.palcheck(s,i,i)
            if r1-l1+1>maxlen:
                l=l1
                r=r1
                maxlen=r1-l1+1
            l1,r1=self.palcheck(s,i,i+1)
            if r1-l1+1>maxlen:
                l=l1
                r=r1
                maxlen=r1-l1+1
        return s[l:r+1]
            
            
    def palcheck(self,s,l,r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1
        return l+1,r-1