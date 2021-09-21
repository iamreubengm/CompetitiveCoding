#Max Consecutive Ones
'''
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example:
    Input: nums = [1,1,0,1,1,1]
    Output: 3
    Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
'''

class Solution:
    def findMaxConsecutiveOnes(self,nums):
        res,c=0,0
        for x in nums:
            if x:
                c+=1
                res=max(res,c)
            else:
                c=0
        return res