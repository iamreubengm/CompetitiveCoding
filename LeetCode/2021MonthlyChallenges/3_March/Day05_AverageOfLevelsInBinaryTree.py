#Average of Levels in Binary Tree
'''
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.

Example:
        Input:
                    3
                   / \
                  9  20
                    /  \
                   15   7
        Output: 
                [3, 14.5, 11]
        Explanation:
                The average value of nodes on level 0 is 3,  on level 1 is 14.5,
                and on level 2 is 11. Hence return [3, 14.5, 11].

Solution:
To solve this, we first use dfs to get the elements at each level. We store each level
and their corresponding elements in a dictionary. Once we get all the elements in each
level, we go through them, and store their averages in a list. Finally we return
the list 'res'.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfLevels(self,root):
        def levels(node,lvl):
            if node:
                if lvl in d:
                    d[lvl].append(node.val)
                else:
                    d[lvl]=[node.val]
                levels(node.right,lvl+1)
                levels(node.left,lvl+1)
        d={}
        res=[]
        levels(root,0)
        for x in d.values():
            res.append(sum(x)/len(x))
        return res