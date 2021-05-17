#Longest String Chain
'''
Given a list of words, each word consists of English lowercase letters.
Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2. For example, "abc" is a predecessor of "abac".
A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.
Return the longest possible length of a word chain with words chosen from the given list of words.

Example:
    Input: words = ["a","b","ba","bca","bda","bdca"]
    Output: 4
    Explanation: One of the longest word chain is "a","ba","bda","bdca".
'''

class Solution:
    def longestStrChain(self,words):
        d={}
        res=1
        for w in sorted(words,key=len):
            d[w]=1
            for i in range(len(w)):
                p=w[:i]+w[i+1:]
                if p in d:
                    d[w]=max(d[p]+1,d[w])
                    res=max(res,d[w])
        return res