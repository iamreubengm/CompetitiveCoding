#Maximum Length of Repeated Subarray
'''
Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

Example:
    Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
    Output: 3
    Explanation: The repeated subarray with maximum length is [3,2,1].
'''

class Solution:
    def findLength(self,nums1,nums2):
        m,n=len(nums1),len(nums2)
        d=[[0]*(n+1) for i in range(m+1)]
        for i in range(m):
            for j in range(n):
                if nums1[i]==nums2[j]:
                    d[i][j]=d[i-1][j-1]+1
        res=0
        for r in d:
            res=max(res,max(r))
        return res