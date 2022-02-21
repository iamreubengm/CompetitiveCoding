#Majority Element
'''
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example:
    Input: nums = [3,2,3]
    Output: 3
'''

class Solution:
    def majorityElement(self,nums):
        d={}
        maj=len(nums)//2
        for x in nums:
            if x not in d:
                d[x]=0
            d[x]+=1
            if d[x]>maj:
                return x