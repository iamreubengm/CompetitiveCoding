#Find All Anagrams in a String
'''
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example:
    Input: s = "cbaebabacd", p = "abc"
    Output: [0,6]
    Explanation:
        The substring with start index = 0 is "cba", which is an anagram of "abc".
        The substring with start index = 6 is "bac", which is an anagram of "abc".
'''

from collections import defaultdict

class Solution:
    def findAnagrams(self,s,p):
        d=defaultdict(int)
        res=[]
        m,n=len(p),len(s)
        if m>n:
            return []
        
        for x in p:
            d[x]+=1
        for i in range(m-1):
            if s[i] in d:
                d[s[i]]-=1
        
        for i in range(-1,n-m+1):
            if i>-1 and s[i] in d:
                d[s[i]]+=1
            if i+m<n and s[i+m] in d:
                d[s[i+m]]-=1
            if all(x==0 for x in d.values()):
                res.append(i+1)
        return res