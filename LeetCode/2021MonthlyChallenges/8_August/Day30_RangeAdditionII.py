#Range Addition II
'''
You are given an m x n matrix M initialized with all 0's and an array of operations ops, where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.
Count and return the number of maximum integers in the matrix after performing all the operations.

Example:
    Input: m = 3, n = 3, ops = [[2,2],[3,3]]
    Output: 4
    Explanation: The maximum integer in M is 2, and there are four of it in M. So return 4.
'''

class Solution:
    def maxCount(self,m,n,ops):
        ops+=[[m,n]]
        minx,miny=float('inf'),float('inf')
        for x,y in ops:
            minx=min(minx,x)
            miny=min(miny,y)
        return minx*miny