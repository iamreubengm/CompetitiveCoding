#Jump Game
'''
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.

Example:
    Input: nums = [2,3,1,1,4]
    Output: true
    Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
'''

class Solution:
    def canJump(self,nums):
        maxj=0
        for i,x in enumerate(nums[:-1]):
            maxj=max(maxj,x+i)
            if x==0 and maxj<=i:
                return False
        return True