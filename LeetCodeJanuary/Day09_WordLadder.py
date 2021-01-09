#Word Ladder
'''
Given two words beginWord and endWord, and a dictionary wordList,
return the length of the shortest transformation sequence from beginWord to endWord,

such that:
Only one letter can be changed at a time.
Each transformed word must exist in the word list.
Return 0 if there is no such transformation sequence.

Example:
    Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
    Output: 5
    Explanation: 
    As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog", return its length 5.
    
Solution:
Create a dictionary which stores all the transformations and the original words.
Using a Queue and a Visited set, go through the trnasformations using BFS to find
the corresponding transformations to reach the end word. 
0 is returned if the end word cannot be reached.
'''

from collections import defaultdict
from collections import deque

class Solution:
    def ladderLength(self,beginWord,endWord,wordList):
        if endWord not in wordList:
            return 0
        n=len(beginWord) #Length of each word
        d=defaultdict(list)
        
        for word in wordList:
            for i in range(n):
                d[word[:i]+'*'+word[i+1:]].append(word)
        
        queue = deque([(beginWord, 1)])
        visited=set()
        visited.add(beginWord)
        while queue:
            current,level=queue.popleft()
            for i in range(n):
                t=current[:i]+"*"+current[i+1:]
                for word in d[t]:
                    if word==endWord:
                        return level+1
                    if word not in visited:
                        visited.add(word)
                        queue.append((word,level+1))
        return 0