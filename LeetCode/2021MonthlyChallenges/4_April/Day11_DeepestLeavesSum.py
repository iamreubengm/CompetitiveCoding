#Deepest Leaves Sum
'''
Given the root of a binary tree, return the sum of values of its deepest leaves.
 
Example:
    Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
    Output: 15

Solution:
We perform a DFS to traverse the entire tree, and at every step, we add the value encountered
to it's corresponding depth in a dictionary. Once the traversal is complete, we simply get the
max value of depth and return the sum of all leaf nodes at that depth from the dictionary.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def deepestLeavesSum(self,root):
        
        def dfs(node,depth):
            if node:
                if depth not in d:
                    d[depth]=[]
                d[depth].append(node.val)
                dfs(node.right,depth+1)
                dfs(node.left,depth+1)

        d={}
        dfs(root,0)
        max_depth=max(d.keys())
        return sum(d[max_depth])


