#Shortest Path in Binary Matrix
'''
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.
A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:
    All the visited cells of the path are 0.
    All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

Example:
    Input: grid = [[0,1],[1,0]]
    Output: 2
'''

from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self,grid):
        n=len(grid)
        neighbors=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        q=deque([(1,0,0)])
        v=set()
        
        while q:
            d,x,y=q.popleft()
            if x==y==n-1:
                return d
            for i,j in neighbors:
                if 0<=x+i<n and 0<=y+j<n and not grid[x+i][y+j] and (x+i,y+j) not in v:
                    v.add((x+i,y+j))
                    q.append((d+1,x+i,y+j))
        return -1