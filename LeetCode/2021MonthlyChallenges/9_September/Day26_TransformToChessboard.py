#Transform to Chessboard
'''
You are given an n x n binary grid board. In each move, you can swap any two rows with each other, or any two columns with each other.
Return the minimum number of moves to transform the board into a chessboard board. If the task is impossible, return -1.
A chessboard board is a board where no 0's and no 1's are 4-directionally adjacent.

Example 1:
    Input: board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
    Output: 2
    Explanation:
        The first move swaps the first and second column.
        The second move swaps the second and third row.
'''

class Solution:
    def movesToChessboard(self,board):
        n=len(board)
        for i in range(n):
            for j in range(n):
                if board[0][0]^board[i][0]^board[0][j]^board[i][j]:
                    return -1
        if not n//2<=sum(board[0])<=(n+1)//2:
            return -1
        if not n//2<=sum(board[i][0] for i in range(n))<=(n+1)//2:
            return -1
        
        col=sum(board[0][i]==i%2 for i in range(n))
        row=sum(board[i][0]==i%2 for i in range(n))
        if n%2:
            if row%2:
                row=n-row
            if col%2:
                col=n-col
        else:
            row=min(row,n-row)
            col=min(col,n-col)
        return (row+col)//2