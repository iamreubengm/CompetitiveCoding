#Largest Divisible Subset
'''
Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:
    answer[i] % answer[j] == 0, or
    answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.

Example:
    Input: nums = [1,2,3]
    Output: [1,2]
    Explanation: [1,3] is also accepted.
'''

class Solution:
    def largestDivisibleSubset(self,nums):
        nums.sort()
        sol=[[x] for x in nums]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]%nums[j]==0 and len(sol[i])<len(sol[j])+1:
                    sol[i]=sol[j]+[nums[i]]
        return max(sol,key=len)