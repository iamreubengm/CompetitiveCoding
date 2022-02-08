#Add Digits
'''
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

Example:
    Input: num = 38
    Output: 2
    Explanation:
        The process is
        38 --> 3 + 8 --> 11
        11 --> 1 + 1 --> 2 
        Since 2 has only one digit, return it.
'''

class Solution:
    def addDigits(self,num):
        while num>9:
            t=0
            while num:
                t+=num%10
                num//=10
            num=t
        return num
    
    def addDigits2(self,num):
        if not num:
            return 0
        return (num-1)%9+1