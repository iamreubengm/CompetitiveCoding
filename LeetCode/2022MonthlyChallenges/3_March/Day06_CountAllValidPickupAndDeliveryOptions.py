#Count All Valid Pickup and Delivery Options
'''
Given n orders, each order consist in pickup and delivery services. 
Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i). 
Since the answer may be too large, return it modulo 10^9 + 7.

Example:
    Input: n = 1
    Output: 1
    Explanation: Unique order (P1, D1), Delivery 1 always is after of Pickup 1.
'''

class Solution:
    def countOrders(self,n):
        res=1
        mod=10**9+7
        for i in range(1,n+1):
            res*=i*(2*i-1)
            res%=mod
        return res