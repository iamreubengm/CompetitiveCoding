#Path Sum III
'''
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.
The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

Example:
    Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
    Output: 3
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def pathSum(self,root,targetSum):
        self.res=0
        self.d=defaultdict(int)
        self.d[targetSum]=1
        self.dfs(root,targetSum,0)
        return self.res
        
    def dfs(self,root,targetSum,cur):
        if not root:
            return None
        cur+=root.val
        self.res+=self.d[cur]
        self.d[cur+targetSum]+=1
        self.dfs(root.left,targetSum,cur)
        self.dfs(root.right,targetSum,cur)
        self.d[cur+targetSum]-=1