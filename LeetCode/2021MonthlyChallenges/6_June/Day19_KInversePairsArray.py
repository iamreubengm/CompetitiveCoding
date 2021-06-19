#K Inverse Pairs Array
'''
For an integer array nums, an inverse pair is a pair of integers [i, j] where 0 <= i < j < nums.length and nums[i] > nums[j].
Given two integers n and k, return the number of different arrays consist of numbers from 1 to n such that there are exactly k inverse pairs.
Since the answer can be huge, return it modulo 109 + 7.

Example:
    Input: n = 3, k = 0
    Output: 1
    Explanation: Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pairs.

    Input: n = 3, k = 1
    Output: 2
    Explanation: The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.
'''

class Solution:
    def kInversePairs(self,n,k):
        d=[[1]*(k+1) for i in range(n+1)]
        s=[[1]*(k+1) for i in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,k+1):
                if i>j:
                    d[i][j]=s[i-1][j]
                else:
                    d[i][j]=(s[i-1][j]-s[i-1][j-i])%(10**9+7)
                s[i][j]=(s[i][j-1]+d[i][j])%(10**9+7)
        return d[-1][-1]