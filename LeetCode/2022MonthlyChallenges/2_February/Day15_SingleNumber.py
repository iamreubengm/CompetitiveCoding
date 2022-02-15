#Single Number
'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example:
    Input: nums = [2,2,1]
    Output: 1
'''

class Solution:
    def singleNumber(self,nums):
        res=0
        for x in nums:
            res^=x
        return res
