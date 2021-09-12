#Reachable Nodes In Subdivided Graph
'''
You are given an undirected graph (the "original graph") with n nodes labeled from 0 to n - 1.
You decide to subdivide each edge in the graph into a chain of nodes, with the number of new nodes varying between each edge.
The graph is given as a 2D array of edges where edges[i] = [ui, vi, cnti] indicates that there is an edge between nodes ui and vi in the original graph,
and cnti is the total number of new nodes that you will subdivide the edge into. Note that cnti == 0 means you will not subdivide the edge.
To subdivide the edge [ui, vi], replace it with (cnti + 1) new edges and cnti new nodes.
The new nodes are x1, x2, ..., xcnti, and the new edges are [ui, x1], [x1, x2], [x2, x3], ..., [xcnti+1, xcnti], [xcnti, vi].
In this new graph, you want to know how many nodes are reachable from the node 0, where a node is reachable if the distance is maxMoves or less.
Given the original graph and maxMoves, return the number of nodes that are reachable from node 0 in the new graph.

Example:
    Input: edges = [[0,1,10],[0,2,1],[1,2,2]], maxMoves = 6, n = 3
    Output: 13
'''

from collections import defaultdict
from heapq import heappush,heappop

class Solution:
    def reachableNodes(self,edges,maxMoves,n):
        d=defaultdict(dict)
        for i,j,k in edges:
            d[i][j]=d[j][i]=k
        q=[(-maxMoves,0)]
        seen={}
        while q:
            move,i=heappop(q)
            if i not in seen:
                seen[i]=-move
                for j in d[i]:
                    m=-move-d[i][j]-1
                    if j not in seen and m>=0:
                        heappush(q,(-m,j))
        res=len(seen)
        for i,j,k in edges:
            res+=min(seen.get(i,0)+seen.get(j,0),d[i][j])
        return res