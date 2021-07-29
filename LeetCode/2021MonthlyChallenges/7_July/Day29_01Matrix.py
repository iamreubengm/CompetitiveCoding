#01 Matrix
'''
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.

Example:
    Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
    Output: [[0,0,0],[0,1,0],[0,0,0]]
'''

class Solution:
    def updateMatrix(self,mat):
        m,n=len(mat),len(mat[0])
        for i in range(m):
            for j in range(n):
                if mat[i][j]:
                    mat[i][j]=float("inf")
                    if i>0 and mat[i-1][j]+1<mat[i][j]:
                        mat[i][j]=mat[i-1][j]+1
                    if j>0 and mat[i][j-1]+1<mat[i][j]:
                        mat[i][j]=mat[i][j-1]+1
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if mat[i][j]!=0:
                    if i+1<m and mat[i+1][j]+1<mat[i][j]:
                        mat[i][j]=mat[i+1][j]+1
                    if j+1<n and mat[i][j+1]+1<mat[i][j]:
                        mat[i][j]=mat[i][j+1]+1
        return mat