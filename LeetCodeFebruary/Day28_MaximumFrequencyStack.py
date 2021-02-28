#Maximum Frequency Stack
'''
Implement FreqStack, a class which simulates the operation of a stack-like data structure.

FreqStack has two functions:
    push(int x), which pushes an integer x onto the stack.
    pop(), which removes and returns the most frequent element in the stack.
If there is a tie for most frequent element, the element closest to the top of the stack is removed and returned.
 

Example:

Input: 
        ["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
        [[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
        
Output: [null,null,null,null,null,null,null,5,7,5,4]

Explanation:
        After making six .push operations, the stack is [5,7,5,7,4,5] from bottom to top.  Then:
        
        pop() -> returns 5, as 5 is the most frequent.
        The stack becomes [5,7,5,7,4].
        
        pop() -> returns 7, as 5 and 7 is the most frequent, but 7 is closest to the top.
        The stack becomes [5,7,5,4].
        
        pop() -> returns 5.
        The stack becomes [5,7,4].
        
        pop() -> returns 4.
        The stack becomes [5,7].
'''
import collections

class FreqStack:
    def __init__(self):
        self.frequency=collections.Counter()
        self.m=collections.defaultdict(list)
        self.maxf=0

    def push(self, x):
        freq,m=self.frequency,self.m
        freq[x]+=1
        self.maxf=max(self.maxf, freq[x])
        m[freq[x]].append(x)
        
    def pop(self):
        freq,m,maxf=self.frequency,self.m,self.maxf
        x=m[maxf].pop()
        if not m[maxf]:
            self.maxf=maxf-1
        freq[x]-=1
        return x
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()