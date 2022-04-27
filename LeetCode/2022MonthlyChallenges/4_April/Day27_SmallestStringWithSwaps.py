#Smallest String With Swaps
'''
You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.
You can swap the characters at any pair of indices in the given pairs any number of times.
Return the lexicographically smallest string that s can be changed to after using the swaps.

Example:
    Input: s = "dcab", pairs = [[0,3],[1,2]]
    Output: "bacd"
    Explaination: 
        Swap s[0] and s[3], s = "bcad"
        Swap s[1] and s[2], s = "bacd"
'''

from collections import defaultdict

class Solution:
    def smallestStringWithSwaps(self,s,pairs):
        class UF:
            def __init__(self, n):
                self.p = list(range(n))
                
            def union(self, x, y):
                self.p[self.find(x)] = self.find(y)
                
            def find(self, x):
                if x != self.p[x]:
                    self.p[x] = self.find(self.p[x])
                return self.p[x]

        uf=UF(len(s))
        res=[]
        m=defaultdict(list)
        for x,y in pairs: 
            uf.union(x,y)
        for i in range(len(s)): 
            m[uf.find(i)].append(s[i])
        for x in m.keys(): 
            m[x].sort(reverse=True)
        for i in range(len(s)): 
            res.append(m[uf.find(i)].pop())
        return ''.join(res)