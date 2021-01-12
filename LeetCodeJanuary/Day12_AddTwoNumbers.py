#Add Two Numbers
'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807.
    
Solution:
Create another linked list with two pointers to it. 
Loop through and calculate the sum of the nodes, and find the carry over and store in carry.
The loop continues as long as there are nodes in either l1 or l2 or there is a carry
yet to be added on.
Finally return the pointer to the newly created linked list.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        ret=l=ListNode(0)
        carry=0
        while l1 or l2 or carry:
            t1=t2=0
            if l1:
                t1=l1.val
                l1=l1.next
            if l2:
                t2=l2.val
                l2=l2.next
            tot=t1+t2+carry
            carry=tot//10
            l.next=ListNode(tot%10)
            l=l.next
            
        return ret.next
            