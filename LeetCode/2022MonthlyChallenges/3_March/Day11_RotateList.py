#Rotate List
'''
Given the head of a linked list, rotate the list to the right by k places.

Example:
    Input: head = [1,2,3,4,5], k = 2
    Output: [4,5,1,2,3]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self,head,k):
        if not head or not head.next:
            return head
        n,last=1,head
        while last.next:
            last=last.next
            n+=1
        if k%n==0:
            return head
        m=head
        for i in range(n-k%n-1):
            m=m.next
        h=m.next
        last.next=head
        m.next=None
        return h