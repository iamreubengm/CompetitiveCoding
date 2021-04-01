#Palindrome Linked List
'''
Given the head of a singly linked list, return true if it is a palindrome.

Example:
    Input: head = [1,2,2,1]
    Output: true

Solution:
A simple solution is to use a list and append all the values of each node in the 
linked list to it. Once the traversal of all nodes is complete, simply check if
the list is the same as it's reversed form.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def isPalindrome(self,head):
        res=[]
        while head:
            res.append(head.val)
            head=head.next
        return res==res[::-1]