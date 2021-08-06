#N-ary Tree Level Order Traversal
'''
Given an n-ary tree, return the level order traversal of its nodes' values.
N-ary Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

Example:
Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]
'''

# Definition for a Node.
#class Node:
#    def __init__(self, val=None, children=None):
#        self.val = val
#        self.children = children

class Solution:
    def levelOrder(self, root):
        def dfs(root,lvl):
            if not root:
                return None
            if lvl==len(res):
                res.append([])
            res[lvl].append(root.val)
            for child in root.children:
                dfs(child,lvl+1)
        res=[]
        dfs(root,0)
        return res