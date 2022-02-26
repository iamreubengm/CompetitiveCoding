#Shortest Path Visiting All Nodes
'''
You have an undirected, connected graph of n nodes labeled from 0 to n - 1. You are given an array graph where graph[i] is a list of all the nodes connected with node i by an edge.
Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.

Example:
    Input: graph = [[1,2,3],[0],[0],[0]]
    Output: 4
    Explanation: One possible path is [1,0,2,0,3]
'''

from collections import deque

class Solution:
    def shortestPathLength(self,graph):
        n=len(graph)
        masks=[1<<i for i in range(n)]
        visited=(1<<n)-1
        queue=deque([(i, masks[i]) for i in range(n)])
        steps=0
        visited_states=[{masks[i]} for i in range(n)]

        while queue:
            count=len(queue)
            while count:
                cur,v =queue.popleft()
                if v==visited:
                    return steps
                for nb in graph[cur]:
                    new=v|masks[nb]
                    if new==visited:
                        return steps+1
                    if new not in visited_states[nb]:
                        visited_states[nb].add(new)
                        queue.append((nb, new))
                count-=1
            steps+=1