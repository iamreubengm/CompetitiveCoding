#Intersection of Two Arrays II
'''
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Example:
    Input: nums1 = [1,2,2,1], nums2 = [2,2]
    Output: [2,2]
'''

class Solution:
    def intersect(self,nums1,nums2):
        d={}
        res=[]
        for x in nums1:
            if x not in d:
                d[x]=0
            d[x]+=1
        for x in nums2:
            if x in d and d[x]:
                res.append(x)
                d[x]-=1
        return res