#Maximum Depth of Binary Tree
'''
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example:
    Input: root = [3,9,20,null,null,15,7]
    Output: 3
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self,root):
        def dfs(node,depth):
            if not node:
                return depth
            return max(dfs(node.left,depth+1),dfs(node.right,depth+1))
        return dfs(root,0)