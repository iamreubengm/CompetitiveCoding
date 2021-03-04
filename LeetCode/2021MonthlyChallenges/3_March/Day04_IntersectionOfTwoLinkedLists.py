#Intersection of Two Linked Lists
'''
Write a program to find the node at which the intersection of two singly linked lists begins.

Notes:
If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Each value on each linked list is in the range [1, 10^9].
Your code should preferably run in O(n) time and use only O(1) memory.

Example:
    
    A: 1 -> 9 -> 1 
                   \
                     2 -> 4
                   /
    B:           3
    
    Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
    Output: Reference of the node with value = 2
    Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
                       From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4].
                       There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.

Solution:
We use two pointers in this solution. Initially, pointer a (pa) and pointer b (pb) refers to the heads of Linked Lists
A and B respectively (headA,headB). We then traverse through both Lists. If one of the pointers reeaches the end of it's
List, we then assign it to the head of the other List, to counter the possible difference in length.
This repeats till both pointers point to the same element or both point to None. The value of 'pa' is then returned.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self,headA,headB):
        pa,pb=headA,headB
        while(pa!=pb):
            pa=pa.next if pa else headB
            pb=pb.next if pb else headA
        return pa