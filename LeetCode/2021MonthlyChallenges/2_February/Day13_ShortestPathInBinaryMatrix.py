#Shortest Path in Binary Matrix
'''
In an N by N square grid, each cell is either empty (0) or blocked (1).

A clear path from top-left to bottom-right has length k if and only if it is composed of cells C_1, C_2, ..., C_k such that:

Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
C_1 is at location (0, 0) (ie. has value grid[0][0])
C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
Return the length of the shortest such clear path from top-left to bottom-right.  If such a path does not exist, return -1.

Example: Input: [[0,0,0],[1,1,0],[1,1,0]]         
         
                 0  0  0
                 1  1  0
                 1  1  0
         
         Output: 4
         
Solution:
We use bfs to find the shortest path. We keep a queue where we append the current distance, and the x,y coordinates.
If the beginning or the end of the matrix is not 0, we return -1. We also keep a visited set to check if the grid has been visited.
We check all neighbors of the current grid, and if we haven't visited them and if it is '0', we add it to visited and
append it to queue. Once we reach the final grid, we return the distance value.
If we haven't returned the value and the loop terminates, we return -1
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