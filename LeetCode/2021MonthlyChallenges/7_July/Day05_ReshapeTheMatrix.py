#Reshape the Matrix
'''
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.
You are given an m x n matrix mat and two integers r and c representing the row number and column number of the wanted reshaped matrix.
The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.
If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example:
    Input: mat = [[1,2],[3,4]], r = 1, c = 4
    Output: [[1,2,3,4]]
'''

class Solution:
    def matrixReshape(self,mat,r,c):
        m,n=len(mat),len(mat[0])
        if m*n!=r*c:
            return mat
        a=[]
        for i in range(m):
            for j in range(n):
                a.append(mat[i][j])
        res=[]
        for i in range(r):
            res.append(a[i*c:(i+1)*c])
        return res