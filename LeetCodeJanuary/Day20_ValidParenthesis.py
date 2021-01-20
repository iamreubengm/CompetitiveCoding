#Valid Parenthesis
'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.
An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
Example:
    Input: s = "()[]{}"
    Output: true
    
Solution:
This is a basic stack problem, where the opening brackets are added onto a stack.
If the closing bracket is encountered, the last element from the stack is popped
and checked if it corresponds to the encountered closing bracket. If the stack is empty
or there is a mismatch, False is returned.
Finally the result is returned based on if the stack is empty or not.
'''

class Solution:
    def isValid(self,s):
        d={'(':')','[':']','{':'}'}
        stack=[]
        for i in s:
            if i in d:
                stack.append(i)
            else:
                if not stack or i!=d[stack.pop()]:
                    return False
        return not stack