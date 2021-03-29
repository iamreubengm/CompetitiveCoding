#Flip Binary Tree To Match Preorder Traversal
'''
You are given the root of a binary tree with n nodes, where each node is uniquely assigned a value from 1 to n.
You are also given a sequence of n values voyage, which is the desired pre-order traversal of the binary tree.
Any node in the binary tree can be flipped by swapping its left and right subtrees.

For example, flipping node 1 will have the following effect:
    1            1
   /\           /\
 2   3  ->     3  2
    /\        /\
   4  5      4 5

Flip the smallest number of nodes so that the pre-order traversal of the tree matches voyage.
Return a list of the values of all flipped nodes. You may return the answer in any order.
If it is impossible to flip the nodes in the tree to make the pre-order traversal match voyage, return the list [-1].

Example:
    Input: root = [1,2,3], voyage = [1,3,2]
        1
       /\
      2  3
    Output: [1]
    Explanation: Flipping node 1 swaps nodes 2 and 3, so the pre-order traversal matches voyage.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def flipMatchVoyage(self,root,voyage):
        res=[]
        stack=[root]
        i=0
        while stack:
            node=stack.pop()
            if not node:
                continue
            if node and node.val!=voyage[i]:
                return [-1]
            i+=1
            if node.right and node.right.val==voyage[i]:
                if node.left:
                    res.append(node.val)
                stack.extend([node.left,node.right])
            else:
                stack.extend([node.right,node.left])
        return res
 

