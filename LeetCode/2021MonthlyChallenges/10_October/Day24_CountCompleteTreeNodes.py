#Count Complete Tree Nodes
'''
Given the root of a complete binary tree, return the number of the nodes in the tree.
According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree,
and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
Design an algorithm that runs in less than O(n) time complexity.

Example:
Input: root = [1,2,3,4,5,6]
Output: 6
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self,root):
        if not root:
            return 0
        left=self.depth(root.left)
        right=self.depth(root.right)
        if left==right:
            return 2**left+self.countNodes(root.right)
        else:
            return 2**right+self.countNodes(root.left)
    
    def depth(self,root):
        if not root:
            return 0
        return 1+self.depth(root.left)