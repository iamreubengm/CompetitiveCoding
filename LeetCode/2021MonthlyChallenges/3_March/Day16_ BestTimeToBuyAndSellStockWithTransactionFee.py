#Best Time to Buy and Sell Stock with Transaction Fee
'''
You are given an array prices where prices[i] is the price of a given stock on the ith day,
and an integer fee representing a transaction fee.
Find the maximum profit you can achieve. You may complete as many transactions as you like,
but you need to pay the transaction fee for each transaction.
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example:
    Input: prices = [1,3,2,8,4,9], fee = 2
    Output: 8
    Explanation: The maximum profit can be achieved by:
                - Buying at prices[0] = 1
                - Selling at prices[3] = 8
                - Buying at prices[4] = 4
                - Selling at prices[5] = 9
                The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
'''

class Solution:
    def maxProfit(self,prices,fee):
        c,h=0,-prices[0]
        for i in range(1,len(prices)):
            c=max(c,h+prices[i]-fee)
            h=max(h,c-prices[i])
        return c