#Basic Calculator
'''
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.
Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example:
    Input: s = "1 + 1"
    Output: 2
'''

class Solution:
    def calculate(self,s):
        res,n,sign=0,0,1
        stack=[]
        ops=['+','-']
        for x in s:
            if x.isdigit():
                n=n*10+int(x)
            elif x in ops:
                res+=sign*n
                n=0
                sign = 1 if x=='+' else -1
            elif x=="(":
                stack.append(res)
                stack.append(sign)
                sign=1
                res=0
            elif x==")":
                res+=sign*n
                res*=stack.pop()
                res+=stack.pop()
                n=0
        return res+n*sign