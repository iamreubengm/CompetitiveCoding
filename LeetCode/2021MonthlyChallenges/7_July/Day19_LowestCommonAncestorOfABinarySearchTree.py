#Lowest Common Ancestor of a Binary Search Tree
'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T
that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example:
    Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
    Output: 6
    Explanation: The LCA of nodes 2 and 8 is 6.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self,root,p,q):
        par=root.val
        if p.val>par and q.val>par:
            return self.lowestCommonAncestor(root.right,p,q)
        elif p.val<par and q.val<par:
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            return root