#Reverse Linked List
'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example:
    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self,head):
        prev=None
        cur=head
        while cur:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
        return prev