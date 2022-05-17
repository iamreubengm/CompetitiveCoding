#Find a Corresponding Node of a Binary Tree in a Clone of That Tree
'''
Given two binary trees original and cloned and given a reference to a node target in the original tree.
The cloned tree is a copy of the original tree.
Return a reference to the same node in the cloned tree.
Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.

Example:
    Input: tree = [7,4,3,null,null,6,19], target = 3
    Output: 3
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self,original,cloned,target):
        o_stack,c_stack=[],[]
        o_node,c_node=original,cloned
        while o_stack or c_node:
            while o_node:
                o_stack.append(o_node)
                c_stack.append(c_node)
                o_node=o_node.left
                c_node=c_node.left
            o_node=o_stack.pop()
            c_node=c_stack.pop()
            
            if o_node==target:
                return c_node
            o_node=o_node.right
            c_node=c_node.right