#Basic Calculator II
'''
Given a string s which represents an expression, evaluate this expression and return its value. 
The integer division should truncate toward zero.
You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].
Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example:
    Input: s = "3+2*2"
    Output: 7
'''

from collections import deque

class Solution:
    def calculate(self,s):
        def precedence(c):
            return c == '*' or c == '/'
        op,num,cur=deque(),deque(),0
        s=s+'#'
        for c in s:
            if c == ' ':
                continue
            elif c.isdigit():
                cur=cur*10+int(c)
            else:
                num.append(cur)
                while op and precedence(c)<=precedence(op[-1]):
                    n1,n2,curOp = num.pop(), num.pop(),op.pop()
                    if curOp=='*':
                        num.append(n2*n1)
                    elif curOp=='/':
                        num.append(n2//n1)
                    elif curOp=='+':
                        num.append(n2+n1)
                    elif curOp=='-':
                        num.append(n2-n1)
                op.append(c)
                cur=0
        return num.pop()