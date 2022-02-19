#Minimize Deviation in Array
'''
You are given an array nums of n positive integers.
You can perform two types of operations on any element of the array any number of times:
    If the element is even, divide it by 2.
        For example, if the array is [1,2,3,4], then you can do this operation on the last element, and the array will be [1,2,3,2].
    If the element is odd, multiply it by 2.
        For example, if the array is [1,2,3,4], then you can do this operation on the first element, and the array will be [2,2,3,4].
The deviation of the array is the maximum difference between any two elements in the array.
Return the minimum deviation the array can have after performing some number of operations.

Example:
    Input: nums = [1,2,3,4]
    Output: 1
    Explanation: You can transform the array to [1,2,3,2], then to [2,2,3,2], then the deviation will be 3 - 2 = 1.
'''

from heapq import heapify,heappop,heappush

class Solution:
    def minimumDeviation(self,nums):
        heap = []
        for x in nums:
            t=x
            while t%2==0:
                t//=2
            heap.append((t,max(x,t*2)))
        
        maxnum=max(i for i,j in heap)
        heapify(heap)
        res=float("inf")

        while len(heap)==len(nums):
            num,limit=heappop(heap)
            res=min(res,maxnum-num)
            if num<limit:
                heappush(heap,(num*2,limit))
                maxnum=max(maxnum,num*2)
        return res