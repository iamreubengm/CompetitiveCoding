#Kth Smallest Element in a Sorted Matrix
'''
Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest element in the matrix.
Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:
    Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
    Output: 13
    Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
'''

class Solution:
    def kthSmallest(self,matrix,k):
        n=len(matrix)
        l,r=matrix[0][0],matrix[-1][-1]
        
        def helper(m):
            j,count=n-1,0
            for i in range(n):
                while j>=0 and matrix[i][j]>m:
                    j-=1
                count+=(j+1)
            return count
        
        while l<r:
            m=l+(r-l)//2
            if helper(m)<k:
                l=m+1
            else:
                r=m
        return l