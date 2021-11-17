#Unique Paths
'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?

Example:
    Input: m = 3, n = 2
    Output: 3
    Explanation:
        From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
        1. Right -> Down -> Down
        2. Down -> Down -> Right
        3. Down -> Right -> Down
'''

class Solution:
    def uniquePaths(self,m,n):
        d=[[1]*n for i in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                d[i][j]=d[i-1][j]+d[i][j-1]
        return d[-1][-1]