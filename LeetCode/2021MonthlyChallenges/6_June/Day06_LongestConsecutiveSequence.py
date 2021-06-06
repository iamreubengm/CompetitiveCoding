#Longest Consecutive Sequence
'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example:
    Input: nums = [100,4,200,1,3,2]
    Output: 4
    Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

    Input: nums = [0,3,7,2,5,8,4,6,0,1]
    Output: 9
'''

class Solution:
    def longestConsecutive(self,nums):
        longest=0
        nums=set(nums) 
        for x in nums:
            if x-1 not in nums:
                cur=x+1
                while cur in nums:
                    cur+=1
                longest=max(longest,cur-x)
        return longest