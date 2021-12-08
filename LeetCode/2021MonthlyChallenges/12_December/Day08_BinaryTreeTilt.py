#Binary Tree Tilt
'''
Given the root of a binary tree, return the sum of every tree node's tilt.
The tilt of a tree node is the absolute difference between the sum of all left subtree node values and all right subtree node values.
If a node does not have a left child, then the sum of the left subtree node values is treated as 0. The rule is similar if there the node does not have a right child.

Example:
    Input: root = [1,2,3]
    Output: 1
    Explanation: 
        Tilt of node 2 : |0-0| = 0 (no children)
        Tilt of node 3 : |0-0| = 0 (no children)
        Tilt of node 1 : |2-3| = 1 (left subtree is just left child, so sum is 2; right subtree is just right child, so sum is 3)
        Sum of every tilt : 0 + 0 + 1 = 1
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findTilt(self,root):
        def dfs(root):
            if not root:
                return 0
            ls,rs=dfs(root.left),dfs(root.right)
            self.tilt+=abs(rs-ls)
            return ls+rs+root.val
        self.tilt=0
        dfs(root)
        return self.tilt