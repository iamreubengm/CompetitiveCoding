#Redundant Connection
'''
In this problem, a tree is an undirected graph that is connected and has no cycles.
You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added.
The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed.
The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.
Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

Example 1:
    Input: edges = [[1,2],[1,3],[2,3]]
    Output: [2,3]
'''

from collections import defaultdict
class Solution:
    def findRedundantConnection(self,edges):
        graph=defaultdict(set)
        
        def dfs(src,t):
            if src not in visited:
                visited.add(src)
                if src==t:
                    return True
                for x in graph[src]:
                    if dfs(x,t):
                        return True
                return False
                
        for u,v in edges:
            visited=set()
            if u in graph and v in graph and dfs(u,v):
                return u,v
            graph[u].add(v)
            graph[v].add(u)