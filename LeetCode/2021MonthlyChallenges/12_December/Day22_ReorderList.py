#Reorder List
'''
You are given the head of a singly linked-list. The list can be represented as:
    L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:
    L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example:
    Input: head = [1,2,3,4]
    Output: [1,4,2,3]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self,head):
        """
        Do not return anything, modify head in-place instead.
        """
        slow,fast=head,head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        
        prev,cur=None,slow.next
        while cur:
            t=cur.next
            cur.next=prev
            prev=cur
            cur=t
        slow.next=None
        
        h1,h2=head,prev
        while h2:
            t=h1.next
            h1.next=h2
            h1=h2
            h2=t