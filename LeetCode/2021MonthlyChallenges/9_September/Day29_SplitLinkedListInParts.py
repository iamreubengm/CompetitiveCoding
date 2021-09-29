#Split Linked List in Parts
'''
Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.
The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.
The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.
Return an array of the k parts.

Example:
    Input: head = [1,2,3], k = 5
    Output: [[1],[2],[3],[],[]]
    Explanation:
        The first element output[0] has output[0].val = 1, output[0].next = null.
        The last element output[4] is null, but its string representation as a ListNode is [].
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def splitListToParts(self,head,k):
        c=head
        n=0
        while c:
            n+=1
            c=c.next
            
        l,rem=n//k,n%k
        res=[]
        c=head
        p=ListNode(0)
        
        for i in range(k):
            if c:
                res.append(c)
                if rem:
                    length=l+1
                    rem-=1
                else:
                    length=l
                for j in range(length):
                    p,c=c,c.next
                p.next=None
            else:
                res.append(None)
        return res