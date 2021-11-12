#Remove Linked List Elements
'''
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

Example:
    Input: head = [1,2,6,3,4,5,6], val = 6
    Output: [1,2,3,4,5]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self,head,val):
        t=ListNode(-1,head)
        cur=t
        while cur.next:
            if cur.next.val==val:
                cur.next=cur.next.next
            else:
                cur=cur.next
        return t.next