#Non-decreasing Array
'''
Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.
We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

Example:
    Input: nums = [4,2,3]
    Output: true
    Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

    Input: nums = [4,2,1]
    Output: false
    Explanation: You can't get a non-decreasing array by modify at most one element.
'''

class Solution:
    def checkPossibility(self,nums):
        flag=-1
        n=len(nums)
        for i in range(n-1):
            if nums[i]>nums[i+1]:
                if flag!=-1:
                    return False
                flag=i
        if flag in [-1,0,n-2]:
            return True
        elif nums[flag-1]<=nums[flag+1] or nums[flag]<=nums[flag+2]:
            return True
        return False