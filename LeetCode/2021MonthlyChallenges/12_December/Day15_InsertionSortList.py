#Insertion Sort List
'''
Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.
The steps of the insertion sort algorithm:
    Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
    At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
    It repeats until no input elements remain.
The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list.
One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.

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
    def insertionSortList(self,head):
        dummy=ListNode(0)
        cur=head
        while cur:
            cnxt=cur.next
            prev,nxt=dummy,dummy.next
            while nxt:
                if nxt.val>cur.val:
                    break
                prev=nxt
                nxt=nxt.next
            cur.next=nxt
            prev.next=cur
            cur=cnxt
        return dummy.next