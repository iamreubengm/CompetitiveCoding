#Summary Ranges
'''
You are given a sorted unique integer array nums.
Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
Each range [a,b] in the list should be output as:
    "a->b" if a != b
    "a" if a == b

Example:
    Input: nums = [0,1,2,4,5,7]
    Output: ["0->2","4->5","7"]
    Explanation:
        The ranges are:
        [0,2] --> "0->2"
        [4,5] --> "4->5"
        [7,7] --> "7"
'''

class Solution:
    def summaryRanges(self,nums):
        res=[]
        i,n=0,len(nums)
        while i<n:
            l=r=i
            while r<n-1 and nums[r]+1==nums[r+1]:
                r+=1
            res.append(str(nums[l])+('->'+str(nums[r]))*(r!=l))
            i=r+1
        return res