#Bitwise AND of Numbers Range
'''
Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.

Example:
    Input: left = 5, right = 7
    Output: 4
'''

class Solution:
    def rangeBitwiseAnd(self,left,right):
        s=0
        while left!=right:
            left>>=1
            right>>=1
            s+=1
        return left<<s