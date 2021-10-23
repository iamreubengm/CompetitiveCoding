#Find Minimum in Rotated Sorted Array II
'''
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,4,4,5,6,7] might become:
    [4,5,6,7,0,1,4] if it was rotated 4 times.
    [0,1,4,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.
You must decrease the overall operation steps as much as possible.

Example:
    Input: nums = [1,3,5]
    Output: 1
'''

class Solution:
    def findMin(self,nums):
        l,h=0,len(nums)-1
        while l<h:
            m=l+(h-l)//2
            if nums[m]>nums[h]:
                l=m+1
            elif nums[m]<nums[l]:
                h=m
                l+=1
            else:
                h-=1
        return nums[l]