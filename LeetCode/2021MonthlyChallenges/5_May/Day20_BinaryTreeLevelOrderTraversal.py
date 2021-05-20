#Binary Tree Level Order Traversal
'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example:
    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[9,20],[15,7]]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self,root):
        
        def dfs(node,level):
            if not node:
                return
            if level not in d:
                d[level]=[]
            d[level].append(node.val)
            dfs(node.left,level+1)
            dfs(node.right,level+1)
        
        d={}
        dfs(root,0)
        return d.values()