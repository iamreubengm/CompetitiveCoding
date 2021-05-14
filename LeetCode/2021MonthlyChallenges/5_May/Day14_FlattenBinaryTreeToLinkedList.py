#Flatten Binary Tree to Linked List
'''
Given the root of a binary tree, flatten the tree into a "linked list":
The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.

Example:
    Input: root = [1,2,5,3,4,null,6]
    Output: [1,null,2,null,3,null,4,null,5,null,6]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self,root):
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.prev=root
        self.flatten(root.left)
        
        t=root.right
        root.right=root.left
        root.left=None
        self.prev.right=t
        self.flatten(t)