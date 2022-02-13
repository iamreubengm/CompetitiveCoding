#Subsets
'''
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example:
    Input: nums = [1,2,3]
    Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
'''

class Solution:
    def subsets(self,nums):
        res=[[]]
        for x in nums:
            t=[]
            for y in res:
                t.append(y+[x])
            res+=t
        return res