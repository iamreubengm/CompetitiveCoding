#Subarray Sum Equals K
'''
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

Example:
    Input: nums = [1,1,1], k = 2
    Output: 2
'''

class Solution:
    def subarraySum(self,nums,k):
        sums={}
        sums[0]=1
        curSum=0
        res=0
        for x in nums:
            curSum+=x
            if curSum-k in sums:
                res+=sums[curSum-k]
            sums[curSum]=sums[curSum]+1 if curSum in sums else 1
        return res