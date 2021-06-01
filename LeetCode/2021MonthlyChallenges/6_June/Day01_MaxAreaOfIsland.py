#Max Area of Island
'''
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.)
You may assume all four edges of the grid are surrounded by water.
The area of an island is the number of cells with a value 1 in the island.
Return the maximum area of an island in grid. If there is no island, return 0.

Example:
    Input: grid =   [[0,0,1,0,0,0,0,1,0,0,0,0,0],
                    [0,0,0,0,0,0,0,1,1,1,0,0,0],
                    [0,1,1,0,1,0,0,0,0,0,0,0,0],
                    [0,1,0,0,1,1,0,0,1,0,1,0,0],
                    [0,1,0,0,1,1,0,0,1,1,1,0,0],
                    [0,0,0,0,0,0,0,0,0,0,1,0,0],
                    [0,0,0,0,0,0,0,1,1,1,0,0,0],
                    [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    Output: 6
    Explanation: The answer is not 11, because the island must be connected 4-directionally.
'''

class Solution:
    def maxAreaOfIsland(self,grid):
        
        def dfs(i,j):
            if 0<=i<m and 0<=j<n and grid[i][j]:
                grid[i][j]=0
                return 1+dfs(i-1,j)+dfs(i,j+1)+dfs(i+1,j)+dfs(i,j-1)
            return 0
        
        m,n=len(grid),len(grid[0])
        maxArea=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    maxArea=max(maxArea,dfs(i,j))
        return maxArea