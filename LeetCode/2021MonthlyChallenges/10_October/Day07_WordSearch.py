#Word Search
'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once.

Example:
    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
    Output: true
'''

class Solution:
    def exist(self,board,word):
        r,c=len(board),len(board[0])
        visited={}
        for i in range(r):
            for j in range(c):
                if self.dfs(board,word,i,j,visited,0):
                    return True
        return False
    
    def dfs(self,board,word,i,j,visited,ind):
        if ind==len(word):
            return True
        if i<0 or i==len(board) or j<0 or j==len(board[0]) or visited.get((i,j)) or word[ind]!=board[i][j]:
            return False
        visited[(i,j)]=True
        moves=[(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
        res=False
        for x in moves:
            res=res or self.dfs(board,word,x[0],x[1],visited,ind+1)
        visited[(i,j)]=False
        return res