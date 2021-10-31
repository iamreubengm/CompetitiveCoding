#Flatten a Multilevel Doubly Linked List
'''
You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer,
which may or may not point to a separate doubly linked list.
These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.
Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.

Example:
    Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
    Output: [1,2,3,7,8,11,12,9,10,4,5,6]
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self,head):
        if not head:
            return
        t=Node(0)
        stack=[head]
        cur=t
        prev=t
        
        while stack:
            root=stack.pop()
            
            if root.next:
                stack.append(root.next)
            if root.child:
                stack.append(root.child)
            cur.next=root
            root.prev=cur
            root.child=None
            cur=root
        
        res=t.next
        res.prev=None
        return res