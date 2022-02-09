#K-diff Pairs in an Array
'''
Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.
A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:
    0 <= i < j < nums.length
    |nums[i] - nums[j]| == k
Notice that |val| denotes the absolute value of val.

Example:
        Input: nums = [3,1,4,1,5], k = 2
        Output: 2
        Explanation:
            There are two 2-diff pairs in the array, (1, 3) and (3, 5).
            Although we have two 1s in the input, we should only return the number of unique pairs.
'''

class Solution:
    def findPairs(self,nums,k):
        d={}
        for x in nums:
            if x not in d:
                d[x]=0
            d[x]+=1
        res=0
        for x in d:
            if k==0 and d[x]>1:
                res+=1
            elif k>0 and x+k in d:
                res+=1
        return res