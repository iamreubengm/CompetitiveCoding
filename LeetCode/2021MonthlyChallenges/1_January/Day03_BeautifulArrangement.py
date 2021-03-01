#Beautiful Arrangement
'''
Suppose you have n integers from 1 to n. We define a beautiful arrangement as an array 
that is constructed by these n numbers successfully if one of the following is true 
for the ith position (1 <= i <= n) in this array:
    -The number at the ith position is divisible by i.
    -i is divisible by the number at the ith position.
Given an integer n, return the number of the beautiful arrangements that you can construct.

Solution:
We use a cache to save the precomputed results.
Recursion is used to calculate the number of Beautiful Arrangements, and added to t.
'''
cache = {}
class Solution(object):
    def countArrangement(self, n):
        def helper(i, X):
            if i==1:
                return 1
            key=(i,X)
            
            if key in cache:
                return cache[key]
            
            t=0
            for j in range(len(X)):
                if X[j]%i==0 or i%X[j]==0:
                    t += helper(i-1, X[:j]+X[j+1:])

            cache[key]=t
            return t
        return helper(n, tuple(range(1,n+1)))