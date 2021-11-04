#Sum of Left Leaves
'''
Given the root of a binary tree, return the sum of all left leaves.

Example:
    Input: root = [3,9,20,null,null,15,7]
    Output: 24
    Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self,root):
        self.res=0
        self.dfs(root,0)
        return self.res
    
    def dfs(self,root,side):
        if not root:
            return
        if not root.left and not root.right and side==-1:
            self.res+=root.val
        self.dfs(root.right,1)
        self.dfs(root.left,-1)