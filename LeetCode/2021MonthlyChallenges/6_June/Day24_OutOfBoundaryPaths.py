#Out of Boundary Paths
'''
There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn].
You are allowed to move the ball to one of the four adjacent four cells in the grid (possibly out of the grid crossing the grid boundary).
You can apply at most maxMove moves to the ball.
Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary.
Since the answer can be very large, return it modulo 109 + 7.

Example:
    Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
    Output: 6
'''

class Solution:
    def findPaths(self,m,n,maxMove,startRow,startColumn):
        d=[[[-1]*(maxMove+1) for i in range(n+1)] for j in range(m+1)]
        
        def solve(i,j,move):
            if move<0:
                return 0
            if i<0 or i>=m or j<0 or j>=n:
                return 1
            if d[i][j][move]!=-1:
                return d[i][j][move]
            
            left=solve(i-1,j,move-1)
            right=solve(i+1,j,move-1)
            top=solve(i,j-1,move-1)
            down=solve(i,j+1,move-1)
            
            d[i][j][move]=left+right+top+down
            return d[i][j][move]
        
        return solve(startRow,startColumn,maxMove)%(10**9+7)