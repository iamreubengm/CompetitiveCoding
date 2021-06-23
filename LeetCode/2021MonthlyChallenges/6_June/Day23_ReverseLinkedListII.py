#Reverse Linked List II
'''
Given the head of a singly linked list and two integers left and right where left <= right,
reverse the nodes of the list from position left to position right,and return the reversed list.

Example:
    Input: head = [1,2,3,4,5], left = 2, right = 4
    Output: [1,4,3,2,5]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self,head,left,right):
        if left==right:
            return head
        h=ListNode(0)
        h.next=head
        prev=h
        for i in range(left-1):
            prev=prev.next
        cur=prev.next
        next=cur.next
        for i in range(right-left):
            t=next.next
            next.next=cur
            cur=next
            next=t
        prev.next.next=next
        prev.next=cur
        return h.next