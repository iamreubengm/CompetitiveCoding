#Partition Equal Subset Sum
'''
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Example:
    Input: nums = [1,5,11,5]
    Output: true
    Explanation: The array can be partitioned as [1, 5, 5] and [11].
'''

from functools import cache

class Solution:
    def canPartition(self,nums):
        @cache
        def subsetSum(s,i):
            if not s:
                return True
            if i>=len(nums) or s<0:
                return False
            return subsetSum(s-nums[i],i+1) or subsetSum(s,i+1)
        tsum=sum(nums)
        return not tsum&1 and subsetSum(tsum//2,0)