#3Sum
'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
'''

class Solution:
    def threeSum(self,nums):
        n=len(nums)
        nums.sort()
        res=[]
        for i in range(n-2):
            if(i and nums[i]==nums[i-1]):
                continue
            target=-1*nums[i]
            l=i+1
            r=n-1
            while(l<r):
                check=nums[l]+nums[r]
                if(check==target):
                    res.append([nums[i],nums[l],nums[r]])
                    while(l<r and nums[r]==nums[r-1]):
                        r-=1
                    l=l+1
                    r=r-1
                elif(check<target):
                    l=l+1
                else:
                    r=r-1
        return res