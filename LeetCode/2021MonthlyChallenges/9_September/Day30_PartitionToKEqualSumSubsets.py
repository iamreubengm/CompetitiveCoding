#Partition to K Equal Sum Subsets
'''
Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

Example:
    Input: nums = [4,3,2,3,5,2,1], k = 4
    Output: true
    Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
'''

class Solution:
    def canPartitionKSubsets(self,nums,k):
        tot=sum(nums)
        nums=sorted(nums,reverse=True)
        if tot%k:
            return False
        t=[tot//k]*k
        
        def dfs(p):
            if p==len(nums):
                return True
            for i in range(k):
                if t[i]>=nums[p]:
                    t[i]-=nums[p]
                    if dfs(p+1):
                        return True
                    t[i]+=nums[p]
            return False

        return dfs(0)