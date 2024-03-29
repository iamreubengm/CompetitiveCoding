#Merge k Sorted Lists
'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example:
    Input: lists = [[1,4,5],[1,3,4],[2,6]]
    Output: [1,1,2,3,4,4,5,6]
    Explanation:
        The linked-lists are:
        [
        1->4->5,
        1->3->4,
        2->6
        ]
        merging them into one sorted list:
        1->1->2->3->4->4->5->6
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from heapq import heappush,heappop
class Solution:
    def mergeKLists(self,lists):
        head=l=ListNode(0)
        heap=[]
        for i,x in enumerate(lists):
            if x:
                heappush(heap,(x.val,i))
        while heap:
            x,i=heappop(heap)
            l.next=ListNode(x)
            l=l.next
            if lists[i].next:
                lists[i]=lists[i].next
                heappush(heap,(lists[i].val,i))
        return head.next