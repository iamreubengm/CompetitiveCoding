#Shift 2D Grid
'''
Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.
In one shift operation:
    Element at grid[i][j] moves to grid[i][j + 1].
    Element at grid[i][n - 1] moves to grid[i + 1][0].
    Element at grid[m - 1][n - 1] moves to grid[0][0].
Return the 2D grid after applying shift operation k times.

Example:
Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[9,1,2],[3,4,5],[6,7,8]]
'''

class Solution:
    def shiftGrid(self,grid,k):
        m,n=len(grid),len(grid[0])
        start=m*n-k%(m*n)
        res=[]
        for i in range(start,m*n+start):
            j=i%(m*n)
            r,c=j//n,j%n
            if not (j-start)%n:
                res.append([])
            res[-1].append(grid[r][c]) 
        return res