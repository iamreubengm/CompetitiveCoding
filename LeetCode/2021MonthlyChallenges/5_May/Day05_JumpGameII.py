#Jump Game II
'''
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.
You can assume that you can always reach the last index.

Example:
    Input: nums = [2,3,1,1,4]
    Output: 2
    Explanation: The minimum number of jumps to reach the last index is 2.
                 Jump 1 step from index 0 to 1, then 3 steps to the last index.
'''

class Solution:
    def jump(self,nums):
        steps=0
        far=0
        curEnd=0
        for i in range(len(nums)-1):
            far=max(far,i+nums[i])
            if i==curEnd:
                steps+=1
                curEnd=far
        return steps