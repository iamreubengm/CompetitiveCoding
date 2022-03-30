#Search a 2D Matrix
'''
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.

Example:
    Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
    Output: true
'''

class Solution:
    def searchMatrix(self,matrix,target):
        m,n=len(matrix[0]),len(matrix)
        l,r=0,m*n-1
        while l<=r:
            mid=(l+r)//2
            num=matrix[mid//m][mid%m]
            if num==target:
                return True
            elif num<target:
                l=mid+1
            else:
                r=mid-1
        return False