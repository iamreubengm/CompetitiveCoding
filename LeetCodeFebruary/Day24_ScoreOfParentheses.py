#Score of Parentheses
'''
Given a balanced parentheses string S, compute the score of the string based on the following rule:
    () has score 1
    AB has score A + B, where A and B are balanced parentheses strings.
    (A) has score 2 * A, where A is a balanced parentheses string.

Example:
    Input: "()()"
    Output: 2
    
    Input: "(()(()))"
    Output: 6

Solution:
We use a stack to solve this question. Everytime we encounter a '(', we append the 'c' value to the stack.
And we then set 'c' to 0 to signify the start of a new nesting. Once we get a ')', we pop the value and 
add it to c, with the minimum value being 1. Finally we return the value of 'c'.
'''

class Solution:
    def scoreOfParentheses(self,S):
        stack=[]
        c=0
        for i in S:
            if i=='(':
                stack.append(c)
                c=0
            else:
                c+=stack.pop()+max(c,1)
        return c

