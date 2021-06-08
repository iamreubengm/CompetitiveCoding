#Construct Binary Tree from Preorder and Inorder Traversal
'''
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree,
construct and return the binary tree.

Example:
    Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
    Output: [3,9,20,null,null,15,7]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self,preorder,inorder):
        def helper(s):
            if inorder and inorder[-1]!=s:
                root=TreeNode(preorder.pop())
                root.left=helper(root.val)
                inorder.pop()
                root.right=helper(s)
                return root
        preorder.reverse()
        inorder.reverse()
        return helper(None)