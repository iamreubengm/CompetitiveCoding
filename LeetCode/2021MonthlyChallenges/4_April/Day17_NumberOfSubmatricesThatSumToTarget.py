#Number of Submatrices That Sum to Target
'''
Given a matrix and a target, return the number of non-empty submatrices that sum to target.
A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.
Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that
is different:for example, if x1 != x1'.

Example:
    Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
    Output: 4
    Explanation: The four 1x1 submatrices that only contain 0.
'''
import collections

class Solution:
    def numSubmatrixSumTarget(self,matrix,target):
        m,n=len(matrix),len(matrix[0])
        for row in matrix:
            for i in range(n-1):
                row[i+1]+=row[i]
        res=0
        for i in range(n):
            for j in range(i,n):
                c=collections.defaultdict(int)
                cur,c[0]=0,1
                for k in range(m):
                    cur+=matrix[k][j]-(matrix[k][i-1] if i > 0 else 0)
                    res+=c[cur-target]
                    c[cur] += 1
        return res