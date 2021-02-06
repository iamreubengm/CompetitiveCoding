#Binary Tree Right Side View
'''
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes
you can see ordered from top to bottom.
Example:
            Input: [1,2,3,null,5,null,4]
            Output: [1, 3, 4]
            Explanation:
            
               1            <---
             /   \
            2     3         <---
             \     \
              5     4       <---

Solution:
We can solve this by performing a simple dfs and storing the values in a dictionary.
The dictionary will store the rightmost node at every level. If a node does not have a 
right child, we perform dfs on the left child and store it in the dictionary.
We finally return the dictionary as a list.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rightSideView(self,root):
        res={}
        
        def dfs(node,height):
            if not node:
                return 
            
            dfs(node.right,height+1)
            if height not in res:
                res[height]=node.val
            dfs(node.left,height+1)
        
        dfs(root,0)
        return [res[i] for i in range(len(res))]