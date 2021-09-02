#Unique Binary Search Trees II
'''
Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n.
Return the answer in any order.

Example:
    Input: n = 3
    Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self,n):
            def dfs(l,r):
                if l>r:
                    return [None]
                if l==r:
                    return [TreeNode(l)]
                res=[]
                for root in range(l,r+1):
                    ln=dfs(l,root-1)
                    rn=dfs(root+1,r)
                    for i in ln:
                        for j in rn:
                            rootNode=TreeNode(root,i,j)
                            res.append(rootNode)
                return res
            return dfs(1,n)