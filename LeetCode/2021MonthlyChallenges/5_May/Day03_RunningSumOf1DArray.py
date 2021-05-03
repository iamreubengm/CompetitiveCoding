#Running Sum of 1d Array
'''
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.

Example:
    Input: nums = [1,2,3,4]
    Output: [1,3,6,10]
    Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
'''

class Solution:
    def runningSum(self,nums):
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        return nums