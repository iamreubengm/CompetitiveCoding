#Coin Change
'''
You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Example:
    Input: coins = [1,2,5], amount = 11
    Output: 3
    Explanation: 11 = 5 + 5 + 1

Solution:
This problem can be solved using DP. We use a list of size amount+1 where each element dp[i]
stores the fewest number of coins used to get to that amount. We update the each element this way
till we get to the end. If the final element is inf, we return -1 as the amount cannot be obtained.
Otherwise, we return the final element.
'''

class Solution:
    def coinChange(self,coins,amount):
        dp=[0]+[float('inf')]*amount
        for i in range(1,amount+1):
            for x in coins:
                if i>=x:
                    dp[i]=min(dp[i],dp[i-x]+1)
        return -1 if dp[-1]==float('inf') else dp[-1] 