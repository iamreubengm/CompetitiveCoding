#Unique Paths III
'''
You are given an m x n integer array grid where grid[i][j] could be:
    1 representing the starting square. There is exactly one starting square.
    2 representing the ending square. There is exactly one ending square.
    0 representing empty squares we can walk over.
    -1 representing obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

Example 1:
    Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
    Output: 2
    Explanation: We have the following two paths: 
        1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
        2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
'''

class Solution:
    def uniquePathsIII(self,grid):
        def dfs(x,y,empty):
            if not (0<=x<m and 0<=y<n and grid[x][y]>=0):
                return
            if grid[x][y]==2:
                self.res+=empty==0
                return
            grid[x][y]=-2
            dfs(x-1,y,empty-1)
            dfs(x+1,y,empty-1)
            dfs(x,y-1,empty-1)
            dfs(x,y+1,empty-1)
            grid[x][y]=0

        m,n=len(grid),len(grid[0])
        empty=1
        self.res=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    x=i
                    y=j
                if not grid[i][j]:
                    empty+=1
        dfs(x,y,empty)
        return self.res