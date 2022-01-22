#Stone Game IV
'''
Alice and Bob take turns playing a game, with Alice starting first.
Initially, there are n stones in a pile. On each player's turn, that player makes a move consisting of removing any non-zero square number of stones in the pile.
Also, if a player cannot make a move, he/she loses the game.
Given a positive integer n, return true if and only if Alice wins the game otherwise return false, assuming both players play optimally.

Example:
    Input: n = 1
    Output: true
    Explanation: Alice can remove 1 stone winning the game because Bob doesn't have any moves.
'''

class Solution:
    def winnerSquareGame(self,n):
        d=[0]*(n+1)
        sq=[]
        cur=1
        for i in range(1,n+1):
            if i==cur*cur:
                sq.append(i)
                cur+=1
                d[i]=1
            else:
                for x in sq:
                    if not d[i-x]:
                        d[i]=1
                        break
        return d[n]