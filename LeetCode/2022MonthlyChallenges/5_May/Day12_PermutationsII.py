#Permutations II
'''
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Example:
    Input: nums = [1,1,2]
    Output:
    [[1,1,2],
    [1,2,1],
    [2,1,1]]
'''

class Solution:
    def dfs(self,nums,path,res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            self.dfs(nums[:i]+nums[i+1:],path+[nums[i]],res)
            
    def permuteUnique(self,nums):
        res=[]
        nums.sort()
        self.dfs(nums,[],res)
        return res