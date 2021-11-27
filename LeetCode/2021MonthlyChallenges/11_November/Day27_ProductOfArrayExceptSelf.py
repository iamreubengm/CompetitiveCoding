#Product of Array Except Self
'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example:
    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]
'''

class Solution:
    def productExceptSelf(self,nums):
        res=[1]*len(nums)
        l,r=1,1
        for i,x in enumerate(nums):
            res[i]*=l
            res[-1-i]*=r
            l*=x
            r*=nums[-1-i]
        return res