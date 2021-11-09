#Number of Valid Words for Each Puzzle
'''
With respect to a given puzzle string, a word is valid if both the following conditions are satisfied:
    word contains the first letter of puzzle.
    For each letter in word, that letter is in puzzle.
        For example, if the puzzle is "abcdefg", then valid words are "faced", "cabbage", and "baggage", while
        invalid words are "beefed" (does not include 'a') and "based" (includes 's' which is not in the puzzle).
Return an array answer, where answer[i] is the number of words in the given word list words that is valid with respect to the puzzle puzzles[i].

Example:
    Input: words = ["aaaa","asas","able","ability","actt","actor","access"], puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
    Output: [1,1,3,2,4,0]
    Explanation: 
        1 valid word for "aboveyz" : "aaaa" 
        1 valid word for "abrodyz" : "aaaa"
        3 valid words for "abslute" : "aaaa", "asas", "able"
        2 valid words for "absoryz" : "aaaa", "asas"
        4 valid words for "actresz" : "aaaa", "asas", "actt", "access"
        There are no valid words for "gaswxyz" cause none of the words in the list contains letter 'g'.
'''

from collections import Counter

class Solution:
    def findNumOfValidWords(self,words,puzzles):
        count=Counter()
        for x in words:
            if len(set(x))>7:
                continue
            m=0
            for c in x:
                m|=1<<(ord(c)-97)
            count[m]+=1
        res=[]
        for p in puzzles:
            bfs=[1<<(ord(p[0])-97)]
            for c in p[1:]:
                bfs+=[m|1<<(ord(c)-97) for m in bfs]
            res.append(sum(count[m] for m in bfs))
        return res