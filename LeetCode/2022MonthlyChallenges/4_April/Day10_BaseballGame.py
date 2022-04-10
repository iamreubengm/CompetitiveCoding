#Baseball Game
'''
You are keeping score for a baseball game with strange rules. The game consists of several rounds, where the scores of past rounds may affect future rounds' scores.
At the beginning of the game, you start with an empty record. You are given a list of strings ops, where ops[i] is the ith operation you must apply to the record and is one of the following:
    An integer x - Record a new score of x.
    "+" - Record a new score that is the sum of the previous two scores. It is guaranteed there will always be two previous scores.
    "D" - Record a new score that is double the previous score. It is guaranteed there will always be a previous score.
    "C" - Invalidate the previous score, removing it from the record. It is guaranteed there will always be a previous score.
Return the sum of all the scores on the record.

Example:
    Input: ops = ["5","2","C","D","+"]
    Output: 30
    Explanation:
        "5" - Add 5 to the record, record is now [5].
        "2" - Add 2 to the record, record is now [5, 2].
        "C" - Invalidate and remove the previous score, record is now [5].
        "D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
        "+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
        The total sum is 5 + 10 + 15 = 30.
'''

class Solution:
    def calPoints(self,ops):
        res=[]
        for i,x in enumerate(ops):
            if x=='+':
                res.append(res[-1]+res[-2])
            elif x=='D':
                res.append(res[-1]*2)
            elif x=='C':
                res.pop()
            else:
                res.append(int(x))
        return sum(res)