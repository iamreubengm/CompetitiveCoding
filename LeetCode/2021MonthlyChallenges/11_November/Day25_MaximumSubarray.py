#Maximum Subarray
'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.

Example:
    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.
'''

class Solution:
    def maxSubArray(self,nums):
        s,ms=0,nums[0]
        for x in nums:
            s=max(x,s+x)
            if s>ms:
                ms=s
        return ms