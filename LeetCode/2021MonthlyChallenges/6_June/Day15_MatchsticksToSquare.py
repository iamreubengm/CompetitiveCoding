#Matchsticks to Square
'''
You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick.
You want to use all the matchsticks to make one square.
You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.
Return true if you can make this square and false otherwise.

Example:
    Input: matchsticks = [1,1,2,2,2]
    Output: true
    Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
'''

class Solution:
    def makesquare(self,matchsticks):
        def dfs(matchsticks,p,target):
            if p==len(matchsticks):
                return True
            for i in range(4):
                if target[i]>=matchsticks[p]:
                    target[i]-=matchsticks[p]
                    if dfs(matchsticks,p+1,target):
                        return True
                    target[i]+=matchsticks[p]
            return False
        
        if len(matchsticks)<4:
            return False
        tsum=sum(matchsticks)
        matchsticks.sort(reverse=True)
        if tsum%4!=0:
            return False
        target=[tsum/4]*4
        return dfs(matchsticks,0,target)