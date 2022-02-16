#Swap Nodes in Pairs
'''
Given a linked list, swap every two adjacent nodes and return its head.
You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example:
    Input: head = [1,2,3,4]
    Output: [2,1,4,3]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self,head):
        dummy=pre=ListNode(0)
        pre.next=head
        while pre.next and pre.next.next:
            a=pre.next
            b=a.next
            pre.next,a.next,b.next=b,b.next,a
            pre=a
        return dummy.next