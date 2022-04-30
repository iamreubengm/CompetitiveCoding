#Evaluate Division
'''
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i].
Each Ai or Bi is a string that represents a single variable.
You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.
Return the answers to all queries. If a single answer cannot be determined, return -1.0.
Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Example:
    Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
    Explanation: 
        Given: a / b = 2.0, b / c = 3.0
        queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
        return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
'''

from collections import defaultdict,deque

class Solution:
    def calcEquation(self,equations,values,queries):
        def calc(x,y):
            if x not in g or y not in g:
                return -1.0
            if x==y:
                return 1.0
            q=deque([(x,1.0)])
            visited={x}
            while q:
                n,cur=q.popleft()
                for child,val in g[n].items():
                    if child in visited:
                        continue
                    nc=cur*val
                    if child==y:
                        return nc
                    g[x][child]=nc
                    g[child][x]=1/nc
                    visited.add(child)
                    q.append((child,nc))
            return -1.0
        
        g=defaultdict(dict)
        for ([x,y],v) in zip(equations,values):
            g[x][y]=v
            g[y][x]=1/v
        res=[]
        for [x,y] in queries:
            res.append(calc(x,y))
        return res