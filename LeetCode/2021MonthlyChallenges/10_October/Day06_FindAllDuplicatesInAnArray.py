#Find All Duplicates in an Array
'''
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice,
return an array of all the integers that appears twice.
You must write an algorithm that runs in O(n) time and uses only constant extra space.

Example:
    Input: nums = [4,3,2,7,8,2,3,1]
    Output: [2,3]
'''

class Solution:
    def findDuplicates(self,nums):
        res=[]
        for x in nums:
            if nums[abs(x)-1]<0:
                res.append(abs(x))
            else:
                nums[abs(x)-1]*=-1
        return res