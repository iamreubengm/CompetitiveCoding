#Valid Sudoku
'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Example:
Input: board = 
        [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
Output: true
'''

class Solution:
    def isValidSudoku(self,board):
        n=9
        rset=[set() for x in range(n)]
        cset=[set() for x in range(n)]
        sset=[set() for x in range(n)]
        
        for r in range(n):
            for c in range(n):
                if board[r][c]==".":
                    continue
                sr,sc=r//3,c//3
                pos=sr*3+sc
                if board[r][c] in rset[r] or board[r][c] in cset[c] or board[r][c] in sset[pos]:
                    return False
                rset[r].add(board[r][c])
                cset[c].add(board[r][c])
                sset[pos].add(board[r][c])
        return True            