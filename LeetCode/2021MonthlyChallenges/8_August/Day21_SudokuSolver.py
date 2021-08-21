#Sudoku Solver
'''
Write a program to solve a Sudoku puzzle by filling the empty cells.
A sudoku solution must satisfy all of the following rules:
    Each of the digits 1-9 must occur exactly once in each row.
    Each of the digits 1-9 must occur exactly once in each column.
    Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

Example:
    Input: 
        [["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]]

    Output:
        [["5","3","4","6","7","8","9","1","2"],
        ["6","7","2","1","9","5","3","4","8"],
        ["1","9","8","3","4","2","5","6","7"],
        ["8","5","9","7","6","1","4","2","3"],
        ["4","2","6","8","5","3","7","9","1"],
        ["7","1","3","9","2","4","8","5","6"],
        ["9","6","1","5","3","7","2","8","4"],
        ["2","8","7","4","1","9","6","3","5"],
        ["3","4","5","2","8","6","1","7","9"]]
'''

class Solution:
    def solveSudoku(self,board):
        """
        Do not return anything, modify board in-place instead.
        """
        r=[[1]*9 for i in range(9)]
        c=[[1]*9 for i in range(9)]
        b=[[1]*9 for i in range(9)]
        v=[]
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    d=int(board[i][j])-1
                    r[i][d]=0
                    c[j][d]=0
                    b[i//3*3+j//3][d]=0
                else:
                    v.append((i,j))
        def backtrack():
            if not v:
                return 1
            i,j=v.pop()
            for d in range(9):
                if r[i][d] and c[j][d] and b[i//3*3+j//3][d]:
                    board[i][j]=str(d+1)
                    r[i][d]=0
                    c[j][d]=0
                    b[i//3*3+j//3][d]=0
                    if backtrack():
                        return 1
                    board[i][j]="."
                    r[i][d]=1
                    c[j][d]=1
                    b[i//3*3+j//3][d]=1
            v.append((i,j))
            return 0
        backtrack()  