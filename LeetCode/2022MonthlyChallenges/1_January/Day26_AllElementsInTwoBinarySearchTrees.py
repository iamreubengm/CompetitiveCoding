#All Elements in Two Binary Search Trees
'''
Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.

Example:
    Input: root1 = [2,1,4], root2 = [1,0,3]
    Output: [0,1,1,2,3,4]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getAllElements(self,root1,root2):
        s1,s2=[],[]
        res=[]
        
        while root1 or root2 or len(s1) or len(s2):
            while root1:
                s1.append(root1)
                root1=root1.left
            while root2:
                s2.append(root2)
                root2=root2.left
            if not len(s2) or (len(s1)>0 and s1[-1].val<=s2[-1].val):
                root1=s1.pop()
                res.append(root1.val)
                root1=root1.right
            else:
                root2=s2.pop()
                res.append(root2.val)
                root2=root2.right
        return res     