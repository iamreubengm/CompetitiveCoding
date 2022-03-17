#Score of Parentheses
'''
Given a balanced parentheses string s, return the score of the string.
The score of a balanced parentheses string is based on the following rule:
    "()" has score 1.
    AB has score A + B, where A and B are balanced parentheses strings.
    (A) has score 2 * A, where A is a balanced parentheses string.
 
Example:
    Input: s = "()"
    Output: 1
'''

class Solution:
    def scoreOfParentheses(self,S):
        stack=[]
        res=0
        for x in S:
            if x=='(':
                stack.append(res)
                res=0
            else:
                res+=stack.pop()+max(res,1)
        return res