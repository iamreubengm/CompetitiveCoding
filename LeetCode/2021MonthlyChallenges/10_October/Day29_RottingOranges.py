#Rotting Oranges
'''
You are given an m x n grid where each cell can have one of three values:
    0 representing an empty cell,
    1 representing a fresh orange, or
    2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example:
    Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
    Output: 4
'''

from collections import deque

class Solution:
    def orangesRotting(self,grid):
        r,c=len(grid),len(grid[0])
        if not r:
            return -1
        fresh=0
        rotten=deque()
        for i in range(r):
            for j in range(c):
                if grid[i][j]==2:
                    rotten.append((i,j))
                elif grid[i][j]:
                    fresh+=1
        mins=0
        while rotten:
            mins+=1
            for i in range(len(rotten)):
                x,y=rotten.popleft()
                for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    if 0<=x+dx<r and 0<=y+dy<c and grid[x+dx][y+dy]==1:
                        fresh-=1
                        grid[x+dx][y+dy]=2
                        rotten.append((x+dx,y+dy))
        if not fresh:
            return max(mins-1,0)
        return -1