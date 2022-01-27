#Maximum XOR of Two Numbers in an Array
'''
Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 <= i <= j < n.

Example:
    Input: nums = [3,10,5,25,2,8]
    Output: 28
    Explanation: The maximum result is 5 XOR 25 = 28.
'''

class Solution:
    def findMaximumXOR(self,nums):
        res=0
        for i in range(32)[::-1]:
            pre=set([x>>i for x in nums])
            res<<=1
            c=res+1
            for x in pre:
                if c^x in pre:
                    res=c
                    break
        return res