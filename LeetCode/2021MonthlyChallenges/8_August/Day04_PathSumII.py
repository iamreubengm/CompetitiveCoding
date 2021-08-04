#Path Sum II
'''
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where each path's sum equals targetSum.
A leaf is a node with no children.

Example:
                    5
                   / \
                  4   8
                 /   / \
                11  13  4
               / \     / \
              7   2   5   1
    Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
    Output: [[5,4,11,2],[5,8,4,5]]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self,root,targetSum):
        def dfs(root,ts,path):
            if not root:
                return None
            ts-=root.val
            path.append(root.val)
            if not root.left and not root.right and not ts:
                res.append([x for x in path])
            else:
                dfs(root.left,ts,path)
                dfs(root.right,ts,path)
            path.pop()
        res=[]
        dfs(root,targetSum,[])
        return res