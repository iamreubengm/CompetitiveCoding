#Swim in Rising Water
'''
On an N x N grid, each square grid[i][j] represents the elevation at that point (i,j).
Now rain starts to fall. At time t, the depth of the water everywhere is t.
You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t.
You can swim infinite distance in zero time. Of course, you must stay within the boundaries of the grid during your swim.
You start at the top left square (0, 0). What is the least time until you can reach the bottom right square (N-1, N-1)?

Example:
    Input: [[0,2],[1,3]]
    Output: 3
    Explanation:
        At time 0, you are in grid location (0, 0).
        You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
        You cannot reach point (1, 1) until time 3.
        When the depth of water is 3, we can swim anywhere inside the grid.
'''

import heapq
class Solution:
    def swimInWater(self,grid):
        n,q,visited,res=len(grid),[(grid[0][0],0,0)],set([(0,0)]),0
        while True:
            h,x,y=heapq.heappop(q)
            res=max(res,h)
            if x==y==n-1:
                return res
            for i,j in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]:
                if 0<=i<n and 0<=j<n and (i,j) not in visited:
                    visited.add((i,j))
                    heapq.heappush(q,(grid[i][j],i,j))