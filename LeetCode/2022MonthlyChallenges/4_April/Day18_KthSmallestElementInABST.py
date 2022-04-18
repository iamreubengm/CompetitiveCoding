#Kth Smallest Element in a BST
'''
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example:
    Input: root = [3,1,4,null,2], k = 1
    Output: 1
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self,root,k):
        res=[]
        self.fn(root, res)
        return res[k-1]
    
    def fn(self,node,res):
        if not node:
            return
        self.fn(node.left,res)
        res.append(node.val)
        self.fn(node.right,res)