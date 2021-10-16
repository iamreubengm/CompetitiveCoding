#Best Time to Buy and Sell Stock III
'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
Find the maximum profit you can achieve. You may complete at most two transactions.
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example:
    Input: prices = [3,3,5,0,0,3,1,4]
    Output: 6
    Explanation:
        Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
        Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
'''

class Solution:
    def maxProfit(self,prices):
        b1=b2=float('inf')
        p1=p2=0
        for x in prices:
            b1=min(b1,x)
            p1=max(p1,x-b1)
            b2=min(b2,x-p1)
            p2=max(p2,x-b2)
        return p2