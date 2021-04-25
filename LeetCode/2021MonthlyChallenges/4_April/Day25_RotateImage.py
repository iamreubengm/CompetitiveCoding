#Rotate Image
'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

Example:
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [[7,4,1],[8,5,2],[9,6,3]]

    1   2   3             7   4   1
    4   5   6      ->     8   5   2
    7   8   9             9   6   3
'''

class Solution:
    def rotate(self,matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.transposeMatrix(matrix)
        self.reverseMatrix(matrix)
    
    def transposeMatrix(self,matrix):
        n=len(matrix)
        for i in range(n):
            for j in range(i,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    
    def reverseMatrix(self,matrix):
        n=len(matrix)
        for i in range(n):
            for j in range(n//2):
                matrix[i][j],matrix[i][-j-1]=matrix[i][-j-1],matrix[i][j]