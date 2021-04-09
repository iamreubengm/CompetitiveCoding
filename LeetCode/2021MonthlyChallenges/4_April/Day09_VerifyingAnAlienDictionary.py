#Verifying an Alien Dictionary
'''
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order.
The order of the alphabet is some permutation of lowercase letters.
Given a sequence of words written in the alien language, and the order of the alphabet,
return true if and only if the given words are sorted lexicographicaly in this alien language.

Example:
    Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
    Output: true
    Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
'''

class Solution:
    def isAlienSorted(self,words,order):
        d={x:i for i,x in enumerate(order)}
        l=[]
        for i in words:
            l.append([d[j] for j in i])
        for x in l:
            for y in l[1:]:
                if y<x:
                    return False
        return True