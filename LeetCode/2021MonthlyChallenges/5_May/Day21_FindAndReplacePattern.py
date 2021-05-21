#Find and Replace Pattern
'''
Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return the answer in any order.
A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.
Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.

Example:
    Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
    Output: ["mee","aqq"]
    Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
                 "ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation, since a and b map to the same letter.
'''

class Solution:
    def findAndReplacePattern(self,words,pattern):
        def find(word):
            d1,d2={},{}
            for w,p in zip(word,pattern):
                if w not in d1:
                    d1[w]=p
                if p not in d2:
                    d2[p]=w
                if (d1[w],d2[p])!=(p,w):
                    return False
            return True
        return filter(find,words)
                    