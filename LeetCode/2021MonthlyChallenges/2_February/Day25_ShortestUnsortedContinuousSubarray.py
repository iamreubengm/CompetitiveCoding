#Shortest Unsorted Continuous Subarray
'''
Given an integer array nums, you need to find one continuous subarray that if you only sort this
subarray in ascending order, then the whole array will be sorted in ascending order.
Return the shortest such subarray and output its length.

Example:
    Input: nums = [2,6,4,8,10,9,15]
    Output: 5
    Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array
    sorted in ascending order.
    
Solution:
This solution involves comparing the list with the sorted version of the array.
If there is no difference in the arrays, we return 0.
We check each element from the left side to see when there is a difference in the arrays.
We then repeat the process from the right side. Finally we find the number of elements
between both these markers and return it.
'''

class Solution:
    def findUnsortedSubarray(self,nums):
        s=sorted(nums)
        if s==nums:
            return 0
        l,r=0,len(nums)-1
        while(s[l]==nums[l]):
            l+=1
        while(s[r]==nums[r]):
            r-=1
        return r-l+1