#Subsets II
'''
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example:
    Input: nums = [1,2,2]
    Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
'''

class Solution:
    def subsetsWithDup(self,nums):
        res=[[]]
        nums.sort()
        cur=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                cur=[x+[nums[i]] for x in cur]
            else:
                cur=[x+[nums[i]] for x in res]
            res+=cur
        return res