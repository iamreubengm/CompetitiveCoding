#3Sum Closest
'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:
    Input: nums = [-1,2,1,-4], target = 1
    Output: 2
    Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

class Solution:
    def threeSumClosest(self,nums,target):
        res=float('inf')
        n=len(nums)
        nums.sort()
        for i in range(n):
            l,r=i+1,n-1
            while l<r:
                s=nums[l]+nums[i]+nums[r]
                if abs(s-target)<abs(res-target):
                    res=s
                if s<=target:
                    l+=1
                elif s>target:
                    r-=1
        return res     