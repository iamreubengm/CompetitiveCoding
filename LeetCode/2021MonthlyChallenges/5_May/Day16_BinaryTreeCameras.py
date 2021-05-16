#Binary Tree Cameras
'''
Given a binary tree, we install cameras on the nodes of the tree. 
Each camera at a node can monitor its parent, itself, and its immediate children.
Calculate the minimum number of cameras needed to monitor all nodes of the tree.

Example:
        0
        /
       C
      / \
     0   0

    Input: [0,0,null,0,0]
    Output: 1
    Explanation: One camera is enough to monitor all nodes if placed as shown.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def minCameraCover(self,root):
        self.res=0
        monitored={None}
        
        def dfs(node,parent):
            if node:
                dfs(node.left,node)
                dfs(node.right,node)
                if not parent and node not in monitored or node.left not in monitored or node.right not in monitored:
                    self.res+=1
                    monitored.update({node,parent,node.left,node.right})
        dfs(root,None)
        return self.res
            