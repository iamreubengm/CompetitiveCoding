#All Paths From Source to Target
'''
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.
The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

Example:
    Input: graph = [[1,2],[3],[3],[]]
    Output: [[0,1,3],[0,2,3]]
    Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
'''

class Solution:
    def allPathsSourceTarget(self,graph):
        def dfs(cur,path):
            if cur==len(graph)-1:
                res.append(path)
            else:
                for i in graph[cur]:
                    dfs(i,path+[i])
        res = []
        dfs(0,[0])
        return res