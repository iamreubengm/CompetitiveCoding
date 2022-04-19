#Recover Binary Search Tree
'''
You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake.
Recover the tree without changing its structure.

Example:
    Input: root = [1,3,null,null,2]
    Output: [3,1,null,null,2]
    Explanation:
        3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverTree(self,root):
        """
        Do not return anything, modify root in-place instead.
        """
        res=self.inorder(root,[])
        n=len(res)
        a=res[0]
        for i in range(1,n):
            if res[i].val < res[i-1].val:
                a=res[i-1]
                break
        b=res[-1]
        for i in range(n-2,-1,-1):
            if res[i].val>res[i+1].val:
                b=res[i+1]
                break
        a.val,b.val = b.val,a.val
    
    def inorder(self,root,arr):
        if not root:
            return
        self.inorder(root.left,arr)
        arr.append(root)
        self.inorder(root.right,arr)
        return arr