#Unique Paths II
'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and space is marked as 1 and 0 respectively in the grid.

Example:
    Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    Output: 2
    Explanation: 
                    0   0   0
                    0   x   0
                    0   0   0

                There is one obstacle in the middle of the 3x3 grid above.
                There are two ways to reach the bottom-right corner:
                1. Right -> Right -> Down -> Down
                2. Down -> Down -> Right -> Right
'''

class Solution:
    def uniquePathsWithObstacles(self,obstacleGrid):
        m,n=len(obstacleGrid),len(obstacleGrid[0])
        d=[[0]*n for x in range(m)]
        if obstacleGrid[0][0]:
            return 0
        d[0][0]=1
        for i in range(m):
            for j in range(n):
                if not obstacleGrid[i][j]:
                    if i>0:
                        d[i][j]+=d[i-1][j]
                    if j>0:
                        d[i][j]+=d[i][j-1]
        return d[-1][-1]