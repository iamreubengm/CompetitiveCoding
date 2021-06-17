#Number of Subarrays with Bounded Maximum
'''
We are given an array nums of positive integers, and two positive integers left and right (left <= right).
Return the number of (contiguous, non-empty) subarrays such that the value of the maximum array element in that subarray is at least left and at most right.

Example:
    Input: 
        nums = [2, 1, 4, 3]
        left = 2
        right = 3
    Output: 3
    Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].
'''
class Solution:
    def numSubarrayBoundedMax(self,nums,left,right):
        lind,rind=-1,-1
        res=0
        for i,x in enumerate(nums):
            if x>=left:
                lind=i
            if x>right:
                rind=i
            res+=lind-rind
        return res