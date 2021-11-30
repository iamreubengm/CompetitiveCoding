#Maximal Rectangle
'''
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:
    Input:
        matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    Output: 6
'''

class Solution:
    def maximalRectangle(self,matrix):
        rows=len(matrix)
        if not rows:
            return 0
        cols=len(matrix[0])
        dp=[[0]*cols for i in range(rows)]
        for i in range(rows):
            acc = 0
            for j in range(cols):
                if matrix[i][j]=="1":
                    acc += 1
                else:
                    acc = 0
                dp[i][j] = acc 
        res=0
        for i in reversed(range(rows)):
            for j in reversed(range(cols)):
                bSide,rSide=dp[i][j],0
                k=i
                while k>-1 and dp[k][j]:
                    bSide=min(bSide,dp[k][j])
                    rSide+=1
                    res=max(res,bSide*rSide)
                    k-=1
        return res