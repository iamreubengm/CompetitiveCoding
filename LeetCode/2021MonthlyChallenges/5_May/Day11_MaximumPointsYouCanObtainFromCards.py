#Maximum Points You Can Obtain from Cards
'''
There are several cards arranged in a row, and each card has an associated number of points The points are given in the integer array cardPoints.
In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.
Your score is the sum of the points of the cards you have taken.
Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

Example:
    Input: cardPoints = [1,2,3,4,5,6,1], k = 3
    Output: 12
    Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score.
                The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.
'''

class Solution:
    def maxScore(self,cardPoints,k):
        minSum,windowSize=float('inf'),len(cardPoints)-k
        cur,j=0,0
        for i,x in enumerate(cardPoints):
            cur+=x
            if i-j+1>windowSize:
                cur-=cardPoints[j]
                j+=1
            if i-j+1==windowSize:
                minSum=min(minSum,cur)
        return sum(cardPoints)-minSum
            