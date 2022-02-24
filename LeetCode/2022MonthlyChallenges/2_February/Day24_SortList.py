#Sort List
'''
Given the head of a linked list, return the list after sorting it in ascending order.

Example:
    Input: head = [4,2,1,3]
    Output: [1,2,3,4]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self,head):
        if not head or not head.next:
            return head
        m=self.getMid(head)
        l=self.sortList(head)
        r=self.sortList(m)
        return self.merge(l,r)
    
    def getMid(self,head):
        slow,fast=head,head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        m=slow.next
        slow.next=None
        return m
    
    def merge(self, head1, head2):
        t=tail=ListNode(None)
        while head1 and head2:
            if head1.val<head2.val:
                tail.next,tail,head1=head1,head1,head1.next
            else:
                tail.next,tail,head2=head2,head2,head2.next
        tail.next=head1 or head2
        return t.next