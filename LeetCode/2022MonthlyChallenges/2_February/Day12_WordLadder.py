#Word Ladder
'''
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
    Every adjacent pair of words differs by a single letter.
    Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
    sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

Example:
    Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
    Output: 5
    Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
'''

from collections import defaultdict,deque

class Solution:
    def ladderLength(self,beginWord,endWord,wordList):
        if endWord not in wordList:
            return 0
        n=len(beginWord)
        d=defaultdict(list)
        for word in wordList:
            for i in range(n):
                d[word[:i]+'*'+word[i+1:]].append(word)
        queue=deque([(beginWord,1)])
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