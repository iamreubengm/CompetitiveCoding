#Two Sum IV - Input is a BST
'''
Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST
such that their sum is equal to the given target.

Example:
    Input: root = [5,3,6,2,4,null,7], k = 9
    Output: true
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findTarget(self,root,k):
        if not root:
            return False
        search=[root]
        seen=set()
        for x in search:
            if k-x.val in seen:
                return True
            seen.add(x.val)
            if x.right:
                search.append(x.right)
            if x.left:
                search.append(x.left)
        return False        