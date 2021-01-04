#Merge Two Sorted Lists
'''
Merge two sorted linked lists and return it as a sorted list. 
The list should be made by splicing together the nodes of the first two lists.

Solution:
We create a new ListNode with two pointers to it, 'head' and 'tail'.
We use a while loop to go through the linked lists as long as they both have
nodes to be visited. We compare their values and add them to the new list one 
by one. Once a list is completed, the other list is added on to the new list.
Finally the head pointer is returned.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self,l1,l2):
        head=tail=ListNode(0)
        while l1 and l2:
            if l1.val<l2.val:
                tail.next=l1
                l1=l1.next
            else:
                tail.next=l2
                l2=l2.next
            tail=tail.next
        tail.next=l1 or l2
        return head.next
        