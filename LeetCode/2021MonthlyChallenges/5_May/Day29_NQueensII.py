#N-Queens II
'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:
    Input: n = 4
    Output: 2
    Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
'''

class Solution:
    def totalNQueens(self,n):
        d1,d2=set(),set()
        cols=set()
        return self.helper(n,d1,d2,cols,0)
        
    def helper(self,n,d1,d2,cols,row):
        if row==n:
            return 1
        count=0
        for col in range(n):
            if row+col in d1 or row-col in d2 or col in cols:
                continue
            d1.add(row+col)
            d2.add(row-col)
            cols.add(col)

            count+=self.helper(n,d1,d2,cols,row+1)

            d1.remove(row+col)
            d2.remove(row-col)
            cols.remove(col)
        return count