#Range Sum Query 2D - Immutable
'''
Given a 2D matrix matrix, handle multiple queries of the following type:
Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Implement the NumMatrix class:
    NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
    int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Example:
    Input
        ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
        [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
    Output
    [null, 8, 11, 12]
    Explanation
        NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
        numMatrix.sumRegion(2, 1, 4, 3); // return 8
        numMatrix.sumRegion(1, 1, 2, 2); // return 11
        numMatrix.sumRegion(1, 2, 2, 4); // return 12
    '''

class NumMatrix:

    def __init__(self,matrix):
        m,n=len(matrix),len(matrix[0])
        self.d=[[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                self.d[i+1][j+1]=self.d[i+1][j]+self.d[i][j+1]-self.d[i][j]+matrix[i][j]

    def sumRegion(self,row1,col1,row2,col2):
        return self.d[row2+1][col2+1]-self.d[row1][col2+1]-self.d[row2+1][col1]+self.d[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)