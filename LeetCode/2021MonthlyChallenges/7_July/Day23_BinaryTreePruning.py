#Binary Tree Pruning
'''
Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has been removed.
A subtree of a node node is node plus every node that is a descendant of node.

Example:
    Input: root = [1,null,0,0,1]
    Output: [1,null,0,null,1]
    Explanation: 
                Only the red nodes satisfy the property "every subtree not containing a 1".
                The diagram on the right represents the answer.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pruneTree(self,root):
        def dfs(node):
            if not node:
                return True
            l,r=dfs(node.left),dfs(node.right)
            if l:
                node.left=None
            if r:
                node.right=None
            return l and r and node.val==0
        
        if not dfs(root):
            return root
        return None