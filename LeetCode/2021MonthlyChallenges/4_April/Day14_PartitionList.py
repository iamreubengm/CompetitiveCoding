#Partition List
'''
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.

Example:
    Input: head = [1,4,3,2,5,2], x = 3
    Output: [1,2,2,4,3,5]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self,head,x):
        lower=lower_head=ListNode(0)
        higher=higher_head=ListNode(0)
        
        while head:
            if head.val>=x:
                higher.next=head
                higher=higher.next
            else:
                lower.next=head
                lower=lower.next
            head=head.next
        
        higher.next=None
        lower.next=higher_head.next
        return lower_head.next
