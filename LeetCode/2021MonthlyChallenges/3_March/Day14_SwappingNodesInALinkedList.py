#Swapping Nodes in a Linked List
'''
You are given the head of a linked list, and an integer k.
Return the head of the linked list after swapping the values of the kth node from the beginning
and the kth node from the end (the list is 1-indexed).

Example:
    Input: head = [1,2,3,4,5], k = 2
    Output: [1,4,3,2,5]
                            1 -> 2 -> 3 -> 4 -> 5
                            1 -> 4 -> 3 -> 2 -> 5

Solution:
We first use a pointer 'fast' to reach the kth node from the start. We then assign
'kth_from_start' to this. We then use the 'kth_from_end' pointer to start from the head,
along with the 'fast' pointer. When the 'fast' pointer reaches the end of the list, the
'kth_from_end' will be at the kth node from the end. We then swap the values.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapNodes(self,head,k):
        fast,kth_from_end=head,head
        for i in range(k-1):
            fast=fast.next
        kth_from_start=fast
        while fast.next:
            kth_from_end=kth_from_end.next
            fast=fast.next
        kth_from_start.val,kth_from_end.val=kth_from_end.val,kth_from_start.val
        return head