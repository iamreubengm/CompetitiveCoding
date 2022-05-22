#Palindromic Substrings
'''
Given a string s, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.

Example:
    Input: s = "abc"
    Output: 3
    Explanation: Three palindromic strings: "a", "b", "c".
'''

class Solution:
    def countSubstrings(self,s):
        n=len(s)
        def subs(i, j):
            while i>=0 and j<n and s[i]==s[j]:
                i,j=i-1,j+1
            return (j-i)//2
        return sum(subs(x,x)+subs(x,x+1) for x in range(n))