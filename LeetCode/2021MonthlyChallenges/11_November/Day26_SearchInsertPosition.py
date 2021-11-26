#Search Insert Position
'''
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

Example:
    Input: nums = [1,3,5,6], target = 5
    Output: 2
'''

class Solution:
    def searchInsert(self,nums,target):
        l,r=0,len(nums)
        while l<r:
            m=(l+r)//2
            if nums[m]>=target:
                r=m
            else:
                l=m+1
        return l