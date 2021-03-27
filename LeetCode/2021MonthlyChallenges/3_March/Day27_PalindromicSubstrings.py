#Palindromic Substrings
'''
Given a string, your task is to count how many palindromic substrings in this string.
The substrings with different start indexes or end indexes are counted as different
substrings even they consist of same characters.

Example:
    Input: "abc"
    Output: 3
    Explanation: Three palindromic strings: "a", "b", "c".
    
    Input: "aaa"
    Output: 6
    Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
'''

class Solution:
    def countSubstrings(self,s):
        n=len(s)
        def subs(i, j):
            while i>=0 and j<n and s[i]==s[j]:
                i,j=i-1,j+1
            return (j-i)//2
        
        return sum(subs(x,x)+subs(x,x+1) for x in range(n))

