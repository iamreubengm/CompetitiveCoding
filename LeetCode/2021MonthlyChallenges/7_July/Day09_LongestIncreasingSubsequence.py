#Longest Increasing Subsequence
'''
Given an integer array nums, return the length of the longest strictly increasing subsequence.
A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.
For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Example:
    Input: nums = [10,9,2,5,3,7,101,18]
    Output: 4
    Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
'''

class Solution:
    def lengthOfLIS(self,nums):
        d=[0]*len(nums)
        res=0
        for x in nums:
            l,r=0,res
            while l!=r:
                m=l+(r-l)//2
                if d[m]<x:
                    l=m+1
                else:
                    r=m
            d[l]=x
            res=max(res,l+1)
        return res