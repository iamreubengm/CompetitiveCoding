#Shortest Path in a Grid with Obstacles Elimination
'''
You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.
Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles.
If it is not possible to find such walk return -1.

Example:
    Input: 
        grid = 
        [[0,0,0],
        [1,1,0],
        [0,0,0],
        [0,1,1],
        [0,0,0]], 
        k = 1
    Output: 6
    Explanation: 
        The shortest path without eliminating any obstacle is 10. 
        The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
'''

from collections import deque

class Solution:
    def shortestPath(self,grid,k):
        m=len(grid)
        n=len(grid[0])
        q=deque([(0,0,0,k)])
        v=set()
        
        while q:
            s,x,y,k=q.popleft()
            if x==n-1 and y==m-1:
                return s
            for dx,dy in (x,y-1),(x,y+1),(x-1,y),(x+1,y):
                if 0<=dx<n and 0<=dy<m and k-grid[dy][dx]>=0:
                    t=(dx,dy,k-grid[dy][dx])
                    if t not in v:
                        v.add(t)
                        q.append((s+1,)+t)
        return -1