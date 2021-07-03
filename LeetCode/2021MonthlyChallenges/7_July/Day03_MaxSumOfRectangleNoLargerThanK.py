#Max Sum of Rectangle No Larger Than K
'''
Given an m x n matrix matrix and an integer k, return the max sum of a rectangle in the matrix such that its sum is no larger than k.
It is guaranteed that there will be a rectangle with a sum no larger than k.

Example:
    Input: matrix = [[1,0,1],[0,-2,3]], k = 2
    Output: 2
    Explanation: Because the sum of the blue rectangle [[0, 1], [-2, 3]] is 2, and 2 is the max number no larger than k (k = 2).
'''

import bisect
class Solution:
    def maxSumSubmatrix(self,matrix,k):
        def maxSum(nums):
            smax=float('-inf')
            scur=0
            prefix=[float('inf')]
            for x in nums:
                bisect.insort(prefix,scur)
                scur+=x
                index=bisect.bisect_left(prefix,scur-k)
                smax=max(smax,scur-prefix[index])
            return smax
        
        m,n=len(matrix),len(matrix[0])
        for i in range(m):
            for j in range(n-1):
                matrix[i][j+1]+=matrix[i][j]
        res=float('-inf')
        for i in range(n):
            for j in range(i,n):
                arr=[matrix[x][j]-(matrix[x][i-1] if i>0 else 0) for x in range(m)]
                res = max(res,maxSum(arr))
        return res