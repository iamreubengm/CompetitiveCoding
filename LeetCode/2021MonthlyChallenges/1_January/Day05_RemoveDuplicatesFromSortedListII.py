#Remove Duplicates from Sorted List II
'''
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list. 
Return the linked list sorted as well.

Solution:
Traverse through the Sorted List. If the value of the current node equals the
value of the next node, a while loop is used to find the end of the duplication.
Once a new element is encountered, 'prev' which currently holds the last value
before the duplications is linked to the new element after the duplicates.
Finally return the List that was stored in the original pointer.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head):
        original=prev=ListNode(0)
        original.next=head
        
        while head and head.next:
            if head.val==head.next.val:
                while head.next and head.val==head.next.val:
                    head=head.next
                head=head.next
                prev.next=head
            else:
                prev=prev.next
                head=head.next
        return original.next