#Linked List Random Node
'''
Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.
Implement the Solution class:
    Solution(ListNode head) Initializes the object with the integer array nums.
    int getRandom() Chooses a node randomly from the list and returns its value. All the nodes of the list should be equally likely to be choosen.

Example:
    Input
        ["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
        [[[1, 2, 3]], [], [], [], [], []]
    Output
        [null, 1, 3, 2, 2, 3]
    Explanation
        Solution solution = new Solution([1, 2, 3]);
        solution.getRandom(); // return 1
        solution.getRandom(); // return 3
        solution.getRandom(); // return 2
        solution.getRandom(); // return 2
        solution.getRandom(); // return 3
        // getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from random import random

class Solution:

    def __init__(self,head):
        self.head=head

    def getRandom(self) -> int:
        n,k=1,1
        head,res=self.head,self.head
        while head.next:
            n+=1
            head=head.next
            if random()<k/n:
                res=res.next
                k+=1
        return res.val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()