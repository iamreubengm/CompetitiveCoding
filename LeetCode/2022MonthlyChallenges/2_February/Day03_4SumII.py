#4Sum II
'''
Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:
    0 <= i, j, k, l < n
    nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

Example:
    Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
    Output: 2
    Explanation:
        The two tuples are:
        1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
        2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
'''

class Solution:
    def fourSumCount(self,nums1,nums2,nums3,nums4):
        d={}
        res=0
        for i in nums1:
            for j in nums2:
                if i+j not in d:
                    d[i+j]=0
                d[i+j]+=1
        for i in nums3:
            for j in nums4:
                if -(i+j) in d:
                    res+=d[-(i+j)]
        return res