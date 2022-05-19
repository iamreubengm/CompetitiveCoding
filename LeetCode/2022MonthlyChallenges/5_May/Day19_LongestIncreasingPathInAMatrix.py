#Longest Increasing Path in a Matrix
'''
Given an m x n integers matrix, return the length of the longest increasing path in matrix.
From each cell, you can either move in four directions: left, right, up, or down.
You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

Example:
    Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
    Output: 4
    Explanation: The longest increasing path is [1, 2, 6, 9].
'''

class Solution:
    def longestIncreasingPath(self,matrix):
        def dfs(i, j):
            if not dp[i][j]: 
                val = matrix[i][j]
                if i and val>matrix[i-1][j]:
                    up=dfs(i-1,j)
                else:
                    up=0
                if i<m-1 and val>matrix[i+1][j]:
                    down=dfs(i+1,j)
                else:
                    down=0
                if j and val>matrix[i][j-1]:
                    left=dfs(i,j-1)
                else:
                    left=0
                if j<n-1 and val>matrix[i][j+1]:
                    right=dfs(i,j+1)
                else:
                    right=0
                dp[i][j]=1+max(up,down,left,right)
            return dp[i][j]
    
        if not matrix:
            return 0
        m,n=len(matrix),len(matrix[0])
        dp=[[0]*n for _ in range(m)]
        res=[]
        for i in range(m):
            for j in range(n):
                res.append(dfs(i,j))
        return max(res)