#Maximum Product of Word Lengths
'''
Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters.
If no such two words exist, return 0.

Example:
    Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
    Output: 16
    Explanation: The two words can be "abcw", "xtfn".
'''
from collections import defaultdict
from itertools import combinations

class Solution:
    def maxProduct(self,words):
        d=defaultdict(int)
        res=0
        for word in words:
            for i in word:
                d[word]|=1<<(ord(i)-97)
        
        for x,y in combinations(d.keys(),2):
            if not d[x]&d[y]:
                res=max(res,len(x)*len(y))
        return res