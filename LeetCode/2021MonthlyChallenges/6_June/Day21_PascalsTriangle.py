#Pascal's Triangle
'''
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example:
    Input: numRows = 5
    Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
'''

class Solution:
    def generate(self,numRows):
        p=[[1]*(i+1) for i in range(numRows)]
        for i in range(numRows):
            for j in range(1,i):
                p[i][j]=p[i-1][j-1]+p[i-1][j]
        return p