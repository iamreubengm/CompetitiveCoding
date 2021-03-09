#Add One Row to Tree
'''
Given the root of a binary tree, then value v and depth d, you need to add a row of nodes with value v at the given depth d.
The root node is at depth 1.

The adding rule is: 
Given a positive integer depth d, for each NOT null tree nodes N in depth d-1,
create two tree nodes with value v as N's left subtree root and right subtree root.
And N's original left subtree should be the left subtree of the new left subtree root,
its original right subtree should be the right subtree of the new right subtree root.
If depth d is 1 that means there is no depth d-1 at all, then create a tree node with value v as
the new root of the whole original tree, and the original tree is the new root's left subtree.

Example:
    Input: 
          A binary tree as following:
                                       4
                                     /   \
                                    2     6
                                   / \   / 
                                  3   1 5   
          v = 1
          d = 2
    
    Output: 
                                       4
                                      / \
                                     1   1
                                    /     \
                                   2       6
                                  / \     / 
                                 3   1   5   
Solution:
We use dfs to build the final tree. The function requires the node, the current height and the direction (L/R : 0/1).
If the height matches the value of 'd', we create a new node and attach 'node' as the left child if direction is left (0),
else we attach it as the right child. If the height is not equal to 'd', we run the function for both child nodes.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def addOneRow(self,root,v,d):
        def dfs(node,height,direction):
            if height==d:
                t=TreeNode(v)
                if direction==1:
                    t.right=node
                else:
                    t.left=node
                return t
            
            if not node:
                return
            node.left=dfs(node.left,height+1,0)
            node.right=dfs(node.right,height+1,1)
            return node
        return dfs(root,1,0)