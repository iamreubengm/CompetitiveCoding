#Number of Matching Subsequences
'''
Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.
A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the
relative order of the remaining characters.
For example, "ace" is a subsequence of "abcde".

Example:
    Input: s = "abcde", words = ["a","bb","acd","ace"]
    Output: 3
    Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
'''
from bisect import bisect_left
from collections import defaultdict
class Solution:
    def numMatchingSubseq(self,s,words):
        def check(word):
            c=0
            for x in word:
                index=bisect_left(d[x],c)
                if index>=len(d[x]):
                    return False
                c=d[x][index]+1
            return True
        d=defaultdict(list)
        for i,x in enumerate(s):
            d[x].append(i)
        res=0
        for x in words:
            res+=check(x)
        return res