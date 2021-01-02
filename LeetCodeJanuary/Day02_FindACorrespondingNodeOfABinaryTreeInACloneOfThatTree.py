#Find a Corresponding Node of a Binary Tree in a Clone of That Tree
'''
Given two binary trees, 'original'  and 'cloned'; and a reference to a node 'target' 
in the original tree, return a reference to the same node in the cloned tree.
Note: You are not allowed to change the trees.

Solution:
This can be solved using Recursive or Iterative means.
The iterative solution is by creating a stack and perform a
DFS Inorder Traversal. If the node in the 'original' tree matches the target,
return the reference to the same node in the 'cloned' tree.
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