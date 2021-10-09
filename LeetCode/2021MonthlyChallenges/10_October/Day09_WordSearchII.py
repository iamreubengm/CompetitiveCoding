#Word Search II
'''
Given an m x n board of characters and a list of strings words, return all words on the board.
Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once in a word.

Example:
    Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
    Output: ["eat","oath"]
'''

from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children=defaultdict(TrieNode)
        self.is_word=False

class Trie:
    def __init__(self):
        self.root=TrieNode()
    
    def insert(self, word):
        node=self.root
        for x in word:
            node=node.children[x]
        node.is_word=True

class Solution:
    def findWords(self,board,words):
        trie=Trie()
        for x in words:
            trie.insert(x)
        m,n=len(board),len(board[0])
        res=[]
        for i in range(m):
            for j in range(n):
                path=[]
                p=''
                self.dfs(board,i,j,trie.root,p,path)
                res+=path
        return res
    
    def dfs(self,board,r,c,node,p,path):
        if node.is_word:
            path.append(p)
            node.is_word=False
        m,n=len(board),len(board[0])
        if r<0 or r>=m or c<0 or c>=n or board[r][c] not in node.children:
            return
        t=board[r][c]
        board[r][c]='#'
        dirs=[(1,0),(-1,0),(0,1),(0,-1)]
        for x in dirs:
            self.dfs(board,r+x[0],c+x[1],node.children[t],p+t,path)
        board[r][c]=t
        
        if not len(node.children[t].children):
            del node.children[t]