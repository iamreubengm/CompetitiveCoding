#Construct Binary Tree from Inorder and Postorder Traversal
'''
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree
and postorder is the postorder traversal of the same tree, construct and return the binary tree.

Example:
    Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
    Output: [3,9,20,null,null,15,7]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self,inorder,postorder):
        self.post=len(postorder)-1
        d={}
        for i,x in enumerate(inorder):
            d[x]=i
        
        def helper(l,r):
            if l>r:
                return None
            root=TreeNode(postorder[self.post])
            self.post-=1
            root.right=helper(d[root.val]+1,r)
            root.left=helper(l,d[root.val]-1)
            return root
        
        return helper(0,len(inorder)-1)