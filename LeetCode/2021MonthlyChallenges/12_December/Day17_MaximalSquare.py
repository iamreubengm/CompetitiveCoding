#Maximal Square
'''
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:
    Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    Output: 4
'''

class Solution:
    def maximalSquare(self,matrix):
        m=len(matrix)
        n=len(matrix[0])
        res=0
        d=[[0]*(n+1) for i in range(m+1)]
        
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if matrix[i][j]=="1":
                    d[i][j]=min(d[i+1][j+1],d[i+1][j],d[i][j+1])+1
                    res=max(res,d[i][j])
        return res*res