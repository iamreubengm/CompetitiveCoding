#Find All Numbers Disappeared in an Array
'''
Given an array nums of n integers where nums[i] is in the range [1, n],
return an array of all the integers in the range [1, n] that do not appear in nums.

Example:
    Input: nums = [4,3,2,7,8,2,3,1]
    Output: [5,6]
'''

class Solution:
    def findDisappearedNumbers(self,nums):
        res=[]
        n=len(nums)
        v=[0]*(n+1)
        for x in nums:
            v[x]=1
        for i in range(1,n+1):
            if not v[i]:
                res.append(i)
        return res