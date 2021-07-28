#Beautiful Array
'''
For some fixed n, an array nums is beautiful if it is a permutation of the integers 1, 2, ..., n, such that:
    For every i < j, there is no k with i < k < j such that nums[k] * 2 = nums[i] + nums[j].
Given n, return any beautiful array nums.  (It is guaranteed that one exists.)

Example:
    Input: n = 4
    Output: [2,1,4,3]
'''

class Solution:
    def beautifulArray(self,n):
        d={1:[1]}
        def dfs(x):
            if x not in d:
                odd=dfs((x+1)//2)
                even=dfs(x//2)
                d[x]=[2*i-1 for i in odd]+[2*i for i in even]
            return d[x]
        return dfs(n)