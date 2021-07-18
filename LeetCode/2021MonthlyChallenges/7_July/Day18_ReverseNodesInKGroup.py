#Reverse Nodes in k-Group
'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example:
    Input: head = [1,2,3,4,5], k = 2
    Output: [2,1,4,3,5]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self,head,k):
        d=ListNode(0)
        d.next=head
        count=0
        cur,nxt,prev=d,d,d
        while cur.next:
            count+=1
            cur=cur.next
        while count>=k:
            cur=n=prev.next
            nxt=cur.next
            for i in range(k-1):
                t=nxt.next
                nxt.next=cur
                cur=nxt
                nxt=t
            prev.next=cur
            n.next=nxt
            prev=n
            count-=k
        return d.next