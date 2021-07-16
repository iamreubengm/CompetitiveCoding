#4Sum
'''
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
    0 <= a, b, c, d < n
    a, b, c, and d are distinct.
    nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example:
    Input: nums = [1,0,-1,0,-2,2], target = 0
    Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
'''

class Solution:
    def fourSum(self,nums,target):
        n=len(nums)
        old=set()
        res=set()
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    l=target-nums[i]-nums[j]-nums[k]
                    if l in old:
                        t=sorted([nums[i],nums[j],nums[k],l])
                        res.add((t[0],t[1],t[2],t[3]))
            old.add(nums[i])
        return res