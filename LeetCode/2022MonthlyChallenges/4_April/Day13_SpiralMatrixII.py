#Spiral Matrix II
'''
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

Example:
    Input: n = 3
    Output: [[1,2,3],[8,9,4],[7,6,5]]
'''

class Solution:
    def generateMatrix(self,n):
        m=[[0]*n for i in range(n)]
        x,y,dx,dy=0,0,1,0
        for i in range(n*n):
            m[y][x]=i+1
            if not 0<=x+dx<n or not 0<=y+dy<n or m[y+dy][x+dx]:
                dx,dy=-dy,dx
            x,y=x+dx,y+dy
        return m