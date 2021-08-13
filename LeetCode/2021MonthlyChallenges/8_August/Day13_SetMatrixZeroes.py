#Set Matrix Zeroes
'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.
You must do it in place.

Example:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
       1 1 1        1 0 1
       1 0 1   ->   0 0 0
       1 1 1        1 0 1
Output: [[1,0,1],[0,0,0],[1,0,1]]
'''

class Solution:
    def setZeroes(self,matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        if not m:
            return
        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    for t in range(m):
                        if matrix[t][j]:
                            matrix[t][j]='x'
                    for t in range(n):
                        if matrix[i][t]:
                            matrix[i][t]='x'
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=='x':
                    matrix[i][j]=0