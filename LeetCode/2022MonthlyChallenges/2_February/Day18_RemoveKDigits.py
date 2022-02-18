#Remove K Digits
'''
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

Example:
    Input: num = "1432219", k = 3
    Output: "1219"
    Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
'''

class Solution:
    def removeKdigits(self,num,k):
        res=[]
        for n in num:
            while res and k and res[-1]>n:
                res.pop()
                k-=1
            res.append(n)
        while k:
            res.pop()
            k-=1
        return ''.join(res).lstrip("0") or "0"