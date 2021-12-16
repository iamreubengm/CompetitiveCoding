#Minimum Height Trees
'''
A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.
Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree,
you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h.
Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).
Return a list of all MHTs' root labels. You can return the answer in any order.
The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

Example:
    Input: n = 4, edges = [[1,0],[1,2],[1,3]]
    Output: [1]
    Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.
'''

from collections import defaultdict

class Solution:
    def findMinHeightTrees(self,n,edges):
        def dfs(i):
            if visited[i]:
                return []
            visited[i]=1
            lpath=max((dfs(x) for x in g[i]),key=len,default=[])+[i]
            visited[i]=0
            return lpath
        g,visited=defaultdict(set),[0]*n
        for u,v in edges:
            g[u].add(v)
            g[v].add(u)
        path=dfs(dfs(0)[0])
        return set([path[len(path)//2],path[(len(path)-1)//2]])