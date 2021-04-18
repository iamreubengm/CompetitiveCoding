#Remove Nth Node From End of List
'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.
Follow up: Could you do this in one pass?

Example:
    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]

Solution:
One approach is to traverse the entire list, find the number of nodes and then delete the requiired node on the second traversal.
A better appraoch is to use two pointers. The fast pointer is first moved n times forward. After that, we move the fast and slow pointers
by one move as long as there exists another node for fast to move to. When the fast pointer moves to the end of the list, the slow pointer
is at the node before the node to be deleted. We simply assign slow.next to slow.next.next to remove the reference to the node to be deleted.
Finally we return the head node.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self,head,n):
        fast=slow=head
        for i in range(n):
            fast=fast.next
        if not fast:
            return head.next
        while fast.next:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return head