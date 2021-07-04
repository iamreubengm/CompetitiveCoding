#Count Vowels Permutation
'''
Given an integer n, your task is to count how many strings of length n can be formed under the following rules:
    Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
    Each vowel 'a' may only be followed by an 'e'.
    Each vowel 'e' may only be followed by an 'a' or an 'i'.
    Each vowel 'i' may not be followed by another 'i'.
    Each vowel 'o' may only be followed by an 'i' or a 'u'.
    Each vowel 'u' may only be followed by an 'a'.
    Since the answer may be too large, return it modulo 10^9 + 7.

Example:
    Input: n = 1
    Output: 5
    Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
'''

class Solution:
    def countVowelPermutation(self,n):
        a,e,i,o,u,x=1,1,1,1,1,10**9+7
        for k in range(n-1):
            a,e,i,o,u=(e+i+u)%x,(a+i)%x,(e+o)%x,i%x,(i+o)%x
        return (a+e+i+o+u)%x