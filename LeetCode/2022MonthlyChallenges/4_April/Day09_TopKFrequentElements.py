#Top K Frequent Elements
'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example:
    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]
'''

from heapq import heapify,heappop

class Solution:
    def topKFrequent(self,nums,k):
        f={}
        res=[]
        for x in nums:
            if x not in f:
                f[x]=0
            f[x]+=1
        h=[[-f,n] for n,f in f.items()]
        heapify(h)
        for i in range(k):
            f,n=heappop(h)
            res.append(n)
        return res