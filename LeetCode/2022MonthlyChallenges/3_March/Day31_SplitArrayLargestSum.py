#Split Array Largest Sum
'''
Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.
Write an algorithm to minimize the largest sum among these m subarrays.

Example:
    Input: nums = [7,2,5,10,8], m = 2
    Output: 18
    Explanation:
        There are four ways to split nums into two subarrays.
        The best way is to split it into [7,2,5] and [10,8],
        where the largest sum among the two subarrays is only 18.
'''

class Solution:
    def splitArray(self,nums,m):
        def canPartition(lsum):
            split=1
            cur=0
            for x in nums:
                cur+=x
                if cur>lsum:
                    split+=1
                    cur=x
            return split<=m

        l=max(nums)
        r=sum(nums)
        res=r
        while l<=r:
            mid=l+(r-l)//2
            if canPartition(mid):
                res=mid
                r=mid-1
            else:
                l=mid+1
        return res