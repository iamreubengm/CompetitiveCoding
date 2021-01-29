#Vertical Order Traversal of a Binary Tree
'''
Given the root of a binary tree, calculate the vertical order traversal of the binary tree.
For each node at position (x, y), its left and right children will be at positions (x - 1, y - 1) and (x + 1, y - 1) respectively.
The vertical order traversal of a binary tree is a list of non-empty reports for each unique x-coordinate from left to right.
Each report is a list of all nodes at a given x-coordinate.
The report should be primarily sorted by y-coordinate from highest y-coordinate to lowest.
If any two nodes have the same y-coordinate in the report, the node with the smaller value should appear earlier.
Return the vertical order traversal of the binary tree.

Example:
    Input: root = [3,9,20,null,null,15,7]
    Output: [[9],[3,15],[20],[7]]
    Explanation: Without loss of generality, we can assume the root node is at position (0, 0):
    The node with value 9 occurs at position (-1, -1).
    The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2).
    The node with value 20 occurs at position (1, -1).
    The node with value 7 occurs at position (2, -2).
'''

# Definition for a binary tree node.
class TreeNode:
   def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right

import collections
class Solution:
    def verticalTraversal(self, root):
        d = collections.defaultdict(list)
        deq = collections.deque()
        deq.append((root,0))
        while deq:
            d1 = collections.defaultdict(list)
            for _ in range(len(deq)):
                node,col = deq.popleft()
                d1[col].append(node.val)
                if node.left:
                    deq.append((node.left,col-1))
                if node.right:
                    deq.append((node.right,col+1))
            for key in d1:
                d[key] += sorted(d1[key])
        return [d[key] for key in sorted(d)]