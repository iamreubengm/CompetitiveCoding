#Valid Parentheses
'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
 
Example:
    Input: s = "()"
    Output: true
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