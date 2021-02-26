#Validate Stack Sequences
'''
Given two sequences pushed and popped with distinct values, return true if and only if this
could have been the result of a sequence of push and pop operations on an initially empty stack.

Example:
    Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
    Output: true
    Explanation: We might do the following sequence:
                push(1), push(2), push(3), push(4), pop() -> 4,
                push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

Solution:
This problem can be solved by simulation. We push the elements from the 'pushed' stack
into our 's' stack. If the element is on top of the 'popped'' stack (i refers to the top
of the stack), we keep popping till it no longer matches. In the end, if the stack is
empty, we return True, else it is False.
'''

class Solution:
    def validateStackSequences(self,pushed,popped):
        s=[]
        i=0
        for x in pushed:
            s.append(x)
            while s and s[-1]==popped[i]:
                s.pop()
                i+=1
        return len(s)==0