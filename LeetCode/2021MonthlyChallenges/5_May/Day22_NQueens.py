#N-Queens
'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle.
Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Example:
    Input: n = 4
    Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
    Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
'''

class Solution:
    def solveNQueens(self,n):
        res,cols,ld,rd=[],set(),set(),set()
        def dfs(r,pos):
            if r==n:
                res.append(['.'*i+'Q'+'.'*(n-i-1) for i in pos])
                return
            for c in range(n):
                if not c in cols and not r-c in ld and not r+c in rd:
                    cols.add(c)
                    ld.add(r-c)
                    rd.add(r+c)
                    dfs(r+1,pos+[c])
                    cols.remove(c)
                    ld.remove(r-c)
                    rd.remove(r+c)
            
        dfs(0,[])
        return res