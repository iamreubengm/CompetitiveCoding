#Largest Plus Sign
'''
You are given an integer n. You have an n x n binary grid grid with all values initially 1's except for some indices given in the array mines.
The ith element of the array mines is defined as mines[i] = [xi, yi] where grid[xi][yi] == 0.
Return the order of the largest axis-aligned plus sign of 1's contained in grid. If there is none, return 0.
An axis-aligned plus sign of 1's of order k has some center grid[r][c] == 1 along with four arms of length k - 1 going up, down, left, and right, and made of 1's.
Note that there could be 0's or 1's beyond the arms of the plus sign, only the relevant area of the plus sign is checked for 1's.

Example:
        1 1 1 1 1 
        1 1 1 1 1
        1 1 1 1 1
        1 1 1 1 1
        1 1 0 1 1
    Input: n = 5, mines = [[4,2]]
    Output: 2
    Explanation: In the above grid, the largest plus sign can only be of order 2. One of them is shown.
'''

class Solution:
    def orderOfLargestPlusSign(self,n,mines):
        d=[[[0]*4 for i in range(n)] for j in range(n)]
        res=0
        mines={(i,j) for i,j in mines}
        
        for i in range(n):
            for j in range(n):
                if (i,j) not in mines:
                    try:
                        d[i][j][0]=d[i-1][j][0]+1
                    except:
                        d[i][j][0]=1
                    try:
                        d[i][j][1]=d[i][j-1][1]+1
                    except:
                        d[i][j][1]=1
        for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):
                if (i,j) not in mines:
                    try:
                        d[i][j][2]=d[i+1][j][2]+1
                    except:
                        d[i][j][2]=1
                    try:
                        d[i][j][3]=d[i][j+1][3]+1
                    except:
                        d[i][j][3]=1
                    res = max(res,min(d[i][j]))
        return res