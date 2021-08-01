#Making A Large Island
'''
You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.
Return the size of the largest island in grid after applying this operation.
An island is a 4-directionally connected group of 1s.

Example:
    Input: grid = [[1,0],[0,1]]
    Output: 3
    Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
'''

from collections import Counter
class Solution:
    def largestIsland(self,grid):
        n=len(grid)
        nl=[[1,0],[-1,0],[0,-1],[0,1]]
        islands=Counter()
        count,res=2,0
        
        def dfs(t,i,j):
            if not 0<=i<n or not 0<=j<n or grid[i][j]!=1:
                return
            islands[t]+=1
            grid[i][j]=t
            for x,y in nl:
                dfs(t,x+i,y+j)
        
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    dfs(count,i,j)
                    count+=1
        
        for i in range(n):
            for j in range(n):
                if not grid[i][j]:
                    neighbors=set()
                    for x,y in nl:
                        if 0<=i+x<n and 0<=j+y<n and grid[i+x][j+y]:
                            neighbors.add(grid[i+x][j+y])
                    res=max(res,sum(islands[c] for c in neighbors)+1)
        if res:
            return res
        return n*n