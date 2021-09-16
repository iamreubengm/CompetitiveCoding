#Spiral Matrix
'''
Given an m x n matrix, return all elements of the matrix in spiral order.

Example:
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [1,2,3,6,9,8,7,4,5]
'''

class Solution:
    def spiralOrder(self,matrix):
        x,y=0,0
        dx,dy=1,0
        res=[]
        m,n=len(matrix),len(matrix[0])

        for i in range(m*n):
            if not 0<=x+dx<n or not 0<=y+dy<m or matrix[y+dy][x+dx]=="x":
                dx,dy=-dy,dx
            res.append(matrix[y][x])
            matrix[y][x]='x'
            x,y=x+dx,y+dy
        return res