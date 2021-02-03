#Linked List Cycle
'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by
continuously following the next pointer. Internally, pos is used to denote the index of the node
that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.

Example:Input: head = [3,2,0,-4], pos = 1
        Output: true
        Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
        
        3 - 2 - 0 - -4
            |        |
            ---------
Solution:
This problem can be easily solved using a two pointer approach.
The fast pointer moves twice as fast as the slow pointer. If there is no loop,
the pointers will never be equal. If there is a loop, the fast pointer will always catch up
to the slow pointer.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self,head):
        s=f=head
        while f and f.next:
            f=f.next.next
            s=s.next
            if f==s:
                return True
        return False