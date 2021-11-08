#Unique Binary Search Trees
'''
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

Example:
    Input: n = 3
    Output: 5
'''

class Solution:
    def numTrees(self,n):
        d=[0]*(n+1)
        d[0],d[1]=1,1
        for i in range(2,n+1):
            for j in range(1,i+1):
                d[i]+=d[j-1]*d[i-j]
        return d[n]