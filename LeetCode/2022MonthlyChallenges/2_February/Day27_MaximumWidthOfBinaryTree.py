#Maximum Width of Binary Tree
'''
Given the root of a binary tree, return the maximum width of the given tree.
The maximum width of a tree is the maximum width among all levels.
The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes are also counted into the length calculation.
It is guaranteed that the answer will in the range of 32-bit signed integer.

Example:
    Input: root = [1,3,2,5,3,null,9]
    Output: 4
    Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def widthOfBinaryTree(self,root):
        level,num,res=1,1,0
        q=deque([[level,num,root]])
        while q:
            [n,l,node]=q.popleft()
            if l>level:
                level,num=l,n
            res=max(res,n-num+1)
            if node.left:
                q.append([n*2,l+1,node.left])
            if node.right:
                q.append([n*2+1,l+1,node.right])
        return res