#Valid Palindrome II
'''
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example:
    Input: s = "aba"
    Output: true
'''

class Solution:
    def validPalindrome(self,s):
        def verify(l,r,flag=False):
            while l<r:
                if s[l]==s[r]:
                    l+=1
                    r-=1
                else:
                    if flag:
                        return False
                    return verify(l+1,r,True) or verify(l,r-1,True)
            return True
        return verify(0,len(s)-1)