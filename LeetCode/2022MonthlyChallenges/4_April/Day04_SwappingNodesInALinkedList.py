#Swapping Nodes in a Linked List
'''
You are given the head of a linked list, and an integer k.
Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

Example:
    Input: head = [1,2,3,4,5], k = 2
    Output: [1,4,3,2,5]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapNodes(self,head,k):
        l=r=head
        for i in range(k-1):
            l=l.next
        node=l
        while node.next:
            r=r.next
            node=node.next
        l.val,r.val=r.val,l.val
        return head