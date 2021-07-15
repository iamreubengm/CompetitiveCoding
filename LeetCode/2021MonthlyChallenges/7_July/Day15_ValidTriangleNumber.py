#Valid Triangle Number
'''
Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

Example:
    Input: nums = [2,2,3,4]
    Output: 3
    Explanation: Valid combinations are: 
                2,3,4 (using the first 2)
                2,3,4 (using the second 2)
                2,2,3
'''

class Solution:
    def triangleNumber(self,nums):
        nums.sort()
        res=0
        for i in range(2,len(nums)):
            l,r=0,i-1
            while l<r:
                if nums[l]+nums[r]>nums[i]:
                    res+=(r-l)
                    r-=1
                else:
                    l+=1
        return res