#Minimum Moves to Equal Array Elements II
'''
Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.
In one move, you can increment or decrement an element of the array by 1.

    Example:
    Input: nums = [1,2,3]
    Output: 2
    Explanation: Only two moves are needed (remember each move increments or decrements one element):
                 [1,2,3]  =>  [2,2,3]  =>  [2,2,2]
'''

class Solution:
    def minMoves2(self,nums):
        nums.sort()
        median=nums[len(nums)//2]
        res=0
        for i in nums:
            res+=abs(i-median)
        return res