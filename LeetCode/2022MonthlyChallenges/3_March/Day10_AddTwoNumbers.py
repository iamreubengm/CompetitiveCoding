#Add Two Numbers
'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self,l1,l2):
        tl1=tl2=ListNode(0)
        carry=0
        while l1 or l2 or carry:
            t1=0
            t2=0
            if l1:
                t1+=l1.val
                l1=l1.next
            if l2:
                t2+=l2.val
                l2=l2.next
            total=t1+t2+carry
            carry=total//10
            tl2.next=ListNode(total%10)
            tl2=tl2.next
        return tl1.next