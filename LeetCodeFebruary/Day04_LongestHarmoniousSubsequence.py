#Longest Harmonious Subsequence
'''
We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.
Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.
A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without
changing theorder of the remaining elements.

Example: Input: nums = [1,3,2,2,5,2,3,7]
         Output: 5
         Explanation: The longest harmonious subsequence is [3,2,2,2,3].

Solution:
For this solution, we use a hashmap that stores the number of times an element appears in the array.
After this, we go through each element, and check if 'element+1' is present.
If so, we take the length of this subsequence and compare it with the current maximum and make the changes accordingly.
'''

class Solution:
    def findLHS(self,nums):
        d={}
        res=0
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in d:
            if i+1 in d:
                res=max(res,d[i]+d[i+1])
        return res

