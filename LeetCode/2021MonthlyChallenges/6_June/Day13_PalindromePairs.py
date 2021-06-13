#Palindrome Pairs
'''
Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list,
so that the concatenation of the two words words[i] + words[j] is a palindrome.

Example:
    Input: words = ["abcd","dcba","lls","s","sssll"]
    Output: [[0,1],[1,0],[3,2],[2,4]]
    Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]

    Input: words = ["bat","tab","cat"]
    Output: [[0,1],[1,0]]
    Explanation: The palindromes are ["battab","tabbat"]
'''

class Solution:
    def palindromePairs(self,words):
        
        def palCheck(s):
            return s==s[::-1]
        
        words={w:i for i,w in enumerate(words)}
        valid=[]
        for w,k in words.items():
            n=len(w)
            for j in range(n+1):
                pref=w[:j]
                suf=w[j:]
                if palCheck(pref):
                    b=suf[::-1]
                    if b!=w and b in words:
                        valid.append([words[b],k])
                if j!=n and palCheck(suf):
                    b=pref[::-1]
                    if b!=w and b in words:
                        valid.append([k,words[b]])
        return valid