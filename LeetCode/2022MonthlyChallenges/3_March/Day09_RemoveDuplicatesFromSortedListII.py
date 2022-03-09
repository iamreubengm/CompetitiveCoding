#Remove Duplicates from Sorted List II
'''
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
Return the linked list sorted as well.

Example:
    Input: head = [1,2,3,3,4,4,5]
    Output: [1,2,5]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self,head):
        t=prev=ListNode(0)
        t.next=head
        while head and head.next:
            if head.val==head.next.val:
                while head.next and head.val==head.next.val:
                    head=head.next
                head=head.next
                prev.next=head
            else:
                prev=prev.next
                head=head.next
        return t.next