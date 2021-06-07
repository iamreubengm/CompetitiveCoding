#Min Cost Climbing Stairs
'''
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.

Example:
    Input: cost = [10,15,20]
    Output: 15
    Explanation: Cheapest is: start on cost[1], pay that cost, and go to the top.
'''

class Solution:
    def minCostClimbingStairs(self,cost):
        dp=[0]*(len(cost)+1)
        for i in range(2,len(cost)+1):
            one=dp[i-1]+cost[i-1]
            two=dp[i-2]+cost[i-2]
            dp[i]=min(one,two)
        return dp[-1]