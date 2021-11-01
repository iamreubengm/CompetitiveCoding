#Surrounded Regions
'''
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:
    Input:
        board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    Output:
        [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
    Explanation:
        Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'.
        Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'.
        Two cells are connected if they are adjacent cells connected horizontally or vertically.
'''

class Solution:
    def solve(self,board):
        """
        Do not return anything, modify board in-place instead.
        """
        m,n=len(board),len(board[0])
        dirs=[(-1,0),(1,0),(0,-1),(0,1)]
        
        def dfs(i,j):
            if 0<=i <m and 0<=j<n and board[i][j]=='O':
                board[i][j]='T'
                for x,y in dirs:
                    dfs(i+x, j+y)
        
        for i in range(m):
            dfs(i,0)
            dfs(i,n-1)
            
        for j in range(1,n-1):
            dfs(0,j)
            dfs(m-1,j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j]=='T':
                    board[i][j]='O'
                else:
                    board[i][j]='X'