#Max Consecutive Ones III
'''
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example:
    Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
    Output: 6
    Explanation: [1,1,1,0,0,1,1,1,1,1,1]
    Bolded numbers (Index 4,5,9) were flipped from 0 to 1. 
'''

class Solution:
    def longestOnes(self,nums,k):
        l,r=0,0
        count,z=0,0
        while r<len(nums):
            if z+(nums[r]==0)<=k:
                z+=(nums[r]==0)
                r+=1
                count=max(count,r-l)
            else:
                z-=(nums[l]==0)
                l+=1
        return count