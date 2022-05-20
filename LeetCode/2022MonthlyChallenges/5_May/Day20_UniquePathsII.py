#Unique Paths II
'''
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m-1][n-1]). The robot can only move either down or right at any point in time.
An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.
Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
The testcases are generated so that the answer will be less than or equal to 2 * 109.

Example:
    Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    Output: 2
    Explanation:
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