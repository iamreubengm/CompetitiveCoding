#Single Element in a Sorted Array
'''
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.
Return the single element that appears only once.
Your solution must run in O(log n) time and O(1) space.

Example:
    Input: nums = [1,1,2,3,3,4,4,8,8]
    Output: 2
'''

class Solution:
    def singleNonDuplicate(self,nums):
        l=0
        r=len(nums)-1
        while(l<r):
            m=l+(r-l)//2
            if (nums[m]!=nums[m+1]) and (nums[m]!=nums[m-1]):
                return nums[m]
            if m%2==0:
                if nums[m]==nums[m-1]:
                    r=m
                else:
                    l=m
            else:
                if nums[m]==nums[m+1]:
                    r=m-1
                else:
                    l=m+1
        return nums[l]