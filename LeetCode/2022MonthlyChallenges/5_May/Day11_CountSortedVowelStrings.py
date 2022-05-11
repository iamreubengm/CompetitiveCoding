#Count Sorted Vowel Strings
'''
Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.
A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.

Example:
    Input: n = 1
    Output: 5
    Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].
'''

class Solution:
    def countVowelStrings(self,n):
        res=0
        for i in range(n+2):
            s=0
            for j in range(i+1):
                s+=j
                res+=s
        return res