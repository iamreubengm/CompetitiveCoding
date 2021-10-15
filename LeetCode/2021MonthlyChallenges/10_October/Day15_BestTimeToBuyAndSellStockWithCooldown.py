#Best Time to Buy and Sell Stock with Cooldown
'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
Find the maximum profit you can achieve. You may complete as many transactions as you like
(i.e., buy one and sell one share of the stock multiple times) with the following restrictions:
    After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example:
    Input: prices = [1,2,3,0,2]
    Output: 3
    Explanation: transactions = [buy, sell, cooldown, buy, sell]
'''

class Solution:
    def maxProfit(self,prices):
        n=len(prices)
        dp=[[0 for i in range(3)] for j in range(n)]
        dp[0][1]-=prices[0]
        for i in range(1,n):
            dp[i][0]=max(dp[i-1][0],dp[i-1][2])
            dp[i][1]=max(dp[i-1][1],dp[i-1][0]-prices[i])
            dp[i][2]=dp[i-1][1]+prices[i]
        return max(dp[-1])