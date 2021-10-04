#Island Perimeter
'''
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
Grid cells are connected horizontally/vertically (not diagonally).
The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island.
One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:
    Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    Output: 16
'''

class Solution:
    def islandPerimeter(self,grid):
        m,n=len(grid),len(grid[0])
        res=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    res+=4
                    if i:
                        res-=grid[i-1][j]
                    if i<m-1:
                        res-=grid[i+1][j]
                    if j:
                        res-=grid[i][j-1]
                    if j<n-1:
                        res-=grid[i][j+1]
        return res