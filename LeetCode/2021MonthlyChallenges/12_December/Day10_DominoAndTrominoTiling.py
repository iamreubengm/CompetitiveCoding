#Domino and Tromino Tiling
'''
You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.
Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 109 + 7.
In a tiling, every square must be covered by a tile.
Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.

Example:
    Input: n = 3
    Output: 5
'''

class Solution:
    def numTilings(self,n):
        m=int(1e9+7)
        a=[0]*(n+1)
        b=[1,1]+[0]*(n-1)
        for i in range(2,n+1):
            a[i]=(b[i-2]+a[i-1])%m
            b[i]=(b[i-1]+b[i-2]+a[i-1]*2)%m
        return b[n]