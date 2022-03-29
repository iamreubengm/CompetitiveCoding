#Find the Duplicate Number
'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.

Example:
    Input: nums = [1,3,4,2,2]
    Output: 2
'''

class Solution:
    def findDuplicate(self,nums):
        s,f=nums[0],nums[0]
        while True:
            s,f=nums[s],nums[nums[f]]
            if s==f:
                break
        s=nums[0]
        while s!=f:
            s,f=nums[s],nums[f]
        return s