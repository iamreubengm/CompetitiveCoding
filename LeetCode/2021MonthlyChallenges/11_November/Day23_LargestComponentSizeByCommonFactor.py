#Largest Component Size by Common Factor
'''
You are given an integer array of unique positive integers nums. Consider the following graph:
    There are nums.length nodes, labeled nums[0] to nums[nums.length - 1],
    There is an undirected edge between nums[i] and nums[j] if nums[i] and nums[j] share a common factor greater than 1.
Return the size of the largest connected component in the graph.

Example:
    Input: nums = [4,6,15,35]
    Output: 4
'''

from collections import defaultdict,Counter
from math import sqrt

class DS:
    def __init__(self,n):
        self.p=[i for i in range(n)]

    def find(self,x):
        if self.p[x]!=x:
            self.p[x]=self.find(self.p[x])
        return self.p[x]

    def union(self,x,y):
        xr,yr=self.find(x),self.find(y)
        self.p[xr]=yr
        
        
class Solution:
    def largestComponentSize(self,nums):
        n=len(nums)
        u=DS(n)
        primes=defaultdict(list)
        for i,x in enumerate(nums):
            pr=self.primes_set(x)
            for q in pr:
                primes[q].append(i)

        for _,indexes in primes.items():
            for i in range(len(indexes)-1):
                u.union(indexes[i],indexes[i+1])
        return max(Counter([u.find(i) for i in range(n)]).values())
        
    def primes_set(self,n):
        for i in range(2,int(sqrt(n))+1):
            if n%i==0:
                return self.primes_set(n//i)|set([i])
        return set([n])