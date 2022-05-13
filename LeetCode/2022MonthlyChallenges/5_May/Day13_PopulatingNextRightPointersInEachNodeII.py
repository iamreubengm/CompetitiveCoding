#Populating Next Right Pointers in Each Node II
'''
Given a binary tree
    struct Node {
    int val;
    Node *left;
    Node *right;
    Node *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.

Example:
    Input: root = [1,2,3,4,5,null,7]
    Output: [1,#,2,3,#,4,5,7,#]
    Explanation:
        Given the above binary tree, your function should populate each next pointer to point to its next right node.
        The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self,root):
        node=root
        while node:
            cur=t=Node(0)
            while node:
                if node.left:
                    cur.next=node.left
                    cur=cur.next
                if node.right:
                    cur.next=node.right
                    cur=cur.next
                node=node.next
            node=t.next
        return root