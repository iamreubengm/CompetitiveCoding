#Search a 2D Matrix II
'''
Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:
Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

Example 1:
    Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
    Output: true

Solution:
As the elements are ordered, we start from the end of the first row, and check if the element is less than the target.
If so, we move one column behind. If the element is greater than the target, we move one row down. If none of the
conditions are met, it means the element is equal to the target, and we return true. If we go through all elements
and haven't returned anything, we return False as the element is not present.
'''

class Solution:
    def searchMatrix(self,matrix,target):
        x,y=0,len(matrix[0])-1
        while x<len(matrix) and y>=0:
            if matrix[x][y]>target:
                y-=1
            elif matrix[x][y]<target:
                x+=1
            else:
                return True
        return False