#Sum of Distances in Tree
'''
There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.
You are given the integer n and the array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.
Return an array answer of length n where answer[i] is the sum of the distances between the ith node in the tree and all other nodes.

Example:
    Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
    Output: [8,12,6,10,10,10]
            0
            / \
        1   2
            /|\
            3 4 5 
    Explanation: 
        The tree is shown above.
        We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
        equals 1 + 1 + 2 + 2 + 2 = 8.
        Hence, answer[0] = 8, and so on.
'''

from collections import defaultdict

class Solution:
    def sumOfDistancesInTree(self,n,edges):
        d=defaultdict(set)
        c=[1]*n
        res=[0]*n
        
        for x,y in edges:
            d[x].add(y)
            d[y].add(x)
        
        def dfs1(node,p):
            for x in d[node]:
                if x!=p:
                    dfs1(x,node)
                    c[node]+=c[x]
                    res[node]+=res[x]+c[x]
        
        def dfs2(node,p):
            for x in d[node]:
                if x!=p:
                    res[x]=res[node]-c[x]+n-c[x]
                    dfs2(x,node)
        
        dfs1(0,-1)
        dfs2(0,-1)
        return res