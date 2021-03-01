#Max Number of K-Sum Pairs
'''
You are given an integer array nums and an integer k.
In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
Return the maximum number of operations you can perform on the array.

Example:
    Input: nums = [1,2,3,4], k = 5
    Output: 2
    Explanation: Starting with nums = [1,2,3,4]:
                - Remove numbers 1 and 4, then nums = [2,3]
                - Remove numbers 2 and 3, then nums = []
                There are no more pairs that sum up to 5, hence a total of 2 operations.
                
Solution:
First cycle through the elements and create a dictionary that stores the number of 
times the element is present in nums.
Then you need to find pairs of elements that sum up to k. That is acheived by taking the
minimum number of times either the number or k-the number is present in the array.
( if nums = [3,3,3,5,5,5,5,5] and k=8, the result is 3 as only 3 pairings can be made)
Since each pair would be counted twice in the previous operation, we divide the result by 2
and return it.
This can be performed using Counters as well
'''

from collections import Counter
class Solution:
    def maxOperations(self,nums,k):
        d={}
        res=0
        for i in nums:
            if i in d:
                d[i]+=1
            elif i<k:
                d[i]=1
        for x in d.keys():
            if x and k-x in d: 
                res+=min(d[x],d[k-x])
        return res//2
    
    def maxOperationsCounter(self,nums,k):
        c=Counter(nums)
        res=0
        for i in c:
            res+=min(c[i],c[k-i])
        return res//2