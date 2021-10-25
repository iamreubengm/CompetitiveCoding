#Min Stack
'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
Implement the MinStack class:
    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.

Example:
Input
    ["MinStack","push","push","push","getMin","pop","top","getMin"]
    [[],[-2],[0],[-3],[],[],[],[]]
Output
    [null,null,null,null,-3,null,0,-2]
Explanation
    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin(); // return -3
    minStack.pop();
    minStack.top();    // return 0
    minStack.getMin(); // return -2
'''

class MinStack:

    def __init__(self):
        self.s=[(-1,float('inf'))]

    def push(self,val):
        curMin=self.getMin()
        if val<curMin:
            curMin=val
        self.s.append((val,curMin))

    def pop(self):
        if len(self.s):
            self.s.pop()

    def top(self):
        if len(self.s):
            return self.s[-1][0]

    def getMin(self):
        return self.s[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()