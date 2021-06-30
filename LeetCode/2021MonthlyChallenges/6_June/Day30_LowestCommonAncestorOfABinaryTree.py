#Lowest Common Ancestor of a Binary Tree
'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T
that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example:
    Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
                3
               / \
              5    1
             / \   / \
            6   2  0  8   
               / \
              7  4 
    Output: 3
    Explanation: The LCA of nodes 5 and 1 is 3.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self,root,p,q):
        stack=[root]
        parent={root: None}
        ancestors=set()
        while p not in parent or q not in parent:
            node=stack.pop()
            if node.left:
                parent[node.left]=node
                stack.append(node.left)
            if node.right:
                parent[node.right]=node
                stack.append(node.right)
        while p:
            ancestors.add(p)
            p=parent[p]
        while q not in ancestors:
            q=parent[q]
        return q