#Stone Game VII
'''
Alice and Bob take turns playing a game, with Alice starting first.
There are n stones arranged in a row. On each player's turn, they can remove either the leftmost stone or the rightmost stone from the row
and receive points equal to the sum of the remaining stones' values in the row. The winner is the one with the higher score when there are no stones left to remove.
Bob found that he will always lose this game (poor Bob, he always loses), so he decided to minimize the score's difference.
Alice's goal is to maximize the difference in the score.
Given an array of integers stones where stones[i] represents the value of the ith stone from the left,
return the difference in Alice and Bob's score if they both play optimally.

Example:
    Input: stones = [5,3,1,4,2]
    Output: 6
    Explanation: 
                - Alice removes 2 and gets 5 + 3 + 1 + 4 = 13 points. Alice = 13, Bob = 0, stones = [5,3,1,4].
                - Bob removes 5 and gets 3 + 1 + 4 = 8 points. Alice = 13, Bob = 8, stones = [3,1,4].
                - Alice removes 3 and gets 1 + 4 = 5 points. Alice = 18, Bob = 8, stones = [1,4].
                - Bob removes 1 and gets 4 points. Alice = 18, Bob = 12, stones = [4].
                - Alice removes 4 and gets 0 points. Alice = 18, Bob = 12, stones = [].
                The score difference is 18 - 12 = 6.
'''

class Solution:
    def stoneGameVII(self,stones):
        n=len(stones)
        dpc,dpl=[0]*n,[0]*n
        for i in range(n-2,-1,-1):
            total=stones[i]
            dpl,dpc=dpc,dpl
            for j in range(i+1,n):
                total+=stones[j]
                dpc[j]=max(total-stones[i]-dpl[j],total-stones[j]-dpc[j-1])
        return dpc[-1]