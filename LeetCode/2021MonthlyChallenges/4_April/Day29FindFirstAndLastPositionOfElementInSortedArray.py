#Find First and Last Position of Element in Sorted Array
'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?

Example:
    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]
'''

class Solution:
    def searchRange(self,nums,target):
        
        def search(nums,x):
            n=len(nums)
            high=n-1
            low=0
            pos=n
            while low<=high:
                mid=(low+high)//2
                if nums[mid]>=x:
                    high=mid-1
                    pos=mid
                else:
                    low=mid+1
            return pos

        first=search(nums,target)
        last=search(nums,target+1)-1
        if first<=last:
            return [first,last]
        else:
            return [-1,-1]