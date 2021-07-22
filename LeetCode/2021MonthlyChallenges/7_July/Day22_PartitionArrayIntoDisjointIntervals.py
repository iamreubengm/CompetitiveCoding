#Partition Array into Disjoint Intervals
'''
Given an array nums, partition it into two (contiguous) subarrays left and right so that:
    Every element in left is less than or equal to every element in right.
    left and right are non-empty.
    left has the smallest possible size.
Return the length of left after such a partitioning.  It is guaranteed that such a partitioning exists.

Example:
    Input: nums = [5,0,3,8,6]
    Output: 3
    Explanation: left = [5,0,3], right = [8,6]
'''

class Solution:
    def partitionDisjoint(self,nums):
        n=len(nums)
        l,r=[0]*n,[0]*n
        
        m=nums[0]
        for i in range(n):
            m=max(m,nums[i])
            l[i]=m
        m=nums[-1]
        for i in range(n-1,-1,-1):
            m=min(m,nums[i])
            r[i]=m
        
        for i in range(1,n):
            if l[i-1]<=r[i]:
                return i