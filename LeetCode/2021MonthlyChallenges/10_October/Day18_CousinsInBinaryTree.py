#Cousins in Binary Tree
'''
Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y,
return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.
Two nodes of a binary tree are cousins if they have the same depth with different parents.
Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.

Example:
    Input: root = [1,2,3,4], x = 4, y = 3
                1
               / \
              2   3
             /
            4 
    Output: false
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isCousins(self,root,x,y):
        def dfs(node,value,depth,parent):
            if not node:
                return
            if node.val==value:
                return parent,depth
            return dfs(node.left,value,depth+1,node) or dfs(node.right,value,depth+1,node)
            
        apar,adep=dfs(root,x,0,None)
        bpar,bdep=dfs(root,y,0,None)
        return apar!=bpar and adep==bdep